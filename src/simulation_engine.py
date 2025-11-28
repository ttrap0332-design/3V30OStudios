"""Simulation Architecture Engine for EVOLVERSE.

This module implements a 60Hz tick rate simulation engine with
double-handshake confirmations for access protocols, matching
both visual and human synchronization requirements.
"""
from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List


class HandshakeState(Enum):
    """States for double-handshake confirmation protocol."""

    PENDING = "pending"
    FIRST_HANDSHAKE = "first_handshake"
    AWAITING_CONFIRMATION = "awaiting_confirmation"
    CONFIRMED = "confirmed"
    FAILED = "failed"
    TIMEOUT = "timeout"


@dataclass
class HandshakeSession:
    """Represents a double-handshake session for access control."""

    session_id: str
    initiator: str
    responder: str
    state: HandshakeState = HandshakeState.PENDING
    first_nonce: str = ""
    second_nonce: str = ""
    created_at: float = field(default_factory=time.time)
    confirmed_at: float | None = None
    timeout_seconds: float = 30.0

    def is_valid(self) -> bool:
        """Check if session is still valid (not timed out)."""
        if self.state == HandshakeState.TIMEOUT:
            return False
        return (time.time() - self.created_at) < self.timeout_seconds


@dataclass
class SimulationTick:
    """Represents a single simulation tick."""

    tick_number: int
    timestamp: float
    delta_time: float
    events: List[Dict] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert tick to dictionary."""
        return {
            "tick_number": self.tick_number,
            "timestamp": self.timestamp,
            "delta_time": self.delta_time,
            "events": self.events,
        }


class DoubleHandshakeProtocol:
    """Implements double-handshake confirmation for access protocols."""

    def __init__(self, timeout_seconds: float = 30.0):
        """Initialize the handshake protocol.

        Args:
            timeout_seconds: Timeout for handshake sessions
        """
        self.sessions: Dict[str, HandshakeSession] = {}
        self.timeout_seconds = timeout_seconds

    def _generate_nonce(self) -> str:
        """Generate a random nonce for handshake."""
        return hashlib.sha256(str(time.time_ns()).encode()).hexdigest()[:32]

    def _generate_session_id(self, initiator: str, responder: str) -> str:
        """Generate a unique session ID."""
        data = f"{initiator}:{responder}:{time.time_ns()}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]

    def initiate_handshake(self, initiator: str, responder: str) -> HandshakeSession:
        """Initiate a new handshake session.

        Args:
            initiator: Identity of the initiating party
            responder: Identity of the responding party

        Returns:
            New HandshakeSession in FIRST_HANDSHAKE state
        """
        session_id = self._generate_session_id(initiator, responder)
        first_nonce = self._generate_nonce()

        session = HandshakeSession(
            session_id=session_id,
            initiator=initiator,
            responder=responder,
            state=HandshakeState.FIRST_HANDSHAKE,
            first_nonce=first_nonce,
            timeout_seconds=self.timeout_seconds,
        )

        self.sessions[session_id] = session
        return session

    def respond_handshake(self, session_id: str) -> HandshakeSession | None:
        """Respond to first handshake.

        Args:
            session_id: The session to respond to

        Returns:
            Updated session or None if not found
        """
        session = self.sessions.get(session_id)
        if session is None:
            return None

        if not session.is_valid():
            session.state = HandshakeState.TIMEOUT
            return session

        if session.state != HandshakeState.FIRST_HANDSHAKE:
            return session

        session.second_nonce = self._generate_nonce()
        session.state = HandshakeState.AWAITING_CONFIRMATION
        return session

    def confirm_handshake(
        self, session_id: str, confirmation_nonce: str
    ) -> HandshakeSession | None:
        """Complete the double handshake with confirmation.

        Args:
            session_id: The session to confirm
            confirmation_nonce: Nonce for final confirmation

        Returns:
            Updated session or None if not found
        """
        session = self.sessions.get(session_id)
        if session is None:
            return None

        if not session.is_valid():
            session.state = HandshakeState.TIMEOUT
            return session

        if session.state != HandshakeState.AWAITING_CONFIRMATION:
            return session

        # Verify confirmation by checking combined nonce hash
        expected = hashlib.sha256(
            (session.first_nonce + session.second_nonce).encode()
        ).hexdigest()[:32]

        if confirmation_nonce == expected:
            session.state = HandshakeState.CONFIRMED
            session.confirmed_at = time.time()
        else:
            session.state = HandshakeState.FAILED

        return session

    def cleanup_expired(self) -> int:
        """Remove expired sessions.

        Returns:
            Number of sessions removed
        """
        expired = [
            sid for sid, session in self.sessions.items() if not session.is_valid()
        ]
        for sid in expired:
            del self.sessions[sid]
        return len(expired)


class SimulationEngine:
    """60Hz simulation engine with visual/human synchronization."""

    # Target tick rate of 60Hz
    TARGET_TICK_RATE = 60
    TARGET_TICK_DURATION = 1.0 / TARGET_TICK_RATE  # ~16.67ms

    def __init__(self):
        """Initialize the simulation engine."""
        self.tick_count: int = 0
        self.start_time: float = 0.0
        self.last_tick_time: float = 0.0
        self.running: bool = False
        self.tick_handlers: List[Callable[[SimulationTick], None]] = []
        self.handshake_protocol = DoubleHandshakeProtocol()
        self.tick_history: List[SimulationTick] = []
        self.max_history: int = 1000

    def register_tick_handler(
        self, handler: Callable[[SimulationTick], None]
    ) -> None:
        """Register a handler to be called on each tick.

        Args:
            handler: Callback function receiving SimulationTick
        """
        self.tick_handlers.append(handler)

    def _process_tick(self, current_time: float) -> SimulationTick:
        """Process a single simulation tick.

        Args:
            current_time: Current timestamp

        Returns:
            The processed SimulationTick
        """
        delta_time = current_time - self.last_tick_time
        self.tick_count += 1

        tick = SimulationTick(
            tick_number=self.tick_count,
            timestamp=current_time,
            delta_time=delta_time,
        )

        # Call registered handlers
        for handler in self.tick_handlers:
            handler(tick)

        # Maintain history
        self.tick_history.append(tick)
        if len(self.tick_history) > self.max_history:
            self.tick_history.pop(0)

        self.last_tick_time = current_time
        return tick

    def run_single_tick(self) -> SimulationTick:
        """Execute a single tick immediately.

        Returns:
            The executed SimulationTick
        """
        current_time = time.time()
        if self.start_time == 0.0:
            self.start_time = current_time
            self.last_tick_time = current_time

        return self._process_tick(current_time)

    def run_ticks(self, count: int) -> List[SimulationTick]:
        """Run a specific number of ticks.

        Args:
            count: Number of ticks to execute

        Returns:
            List of executed SimulationTicks
        """
        ticks = []
        for _ in range(count):
            tick = self.run_single_tick()
            ticks.append(tick)
            # Sleep to maintain 60Hz rate
            time.sleep(self.TARGET_TICK_DURATION)
        return ticks

    def run_duration(self, seconds: float) -> List[SimulationTick]:
        """Run simulation for a specific duration.

        Args:
            seconds: Duration to run in seconds

        Returns:
            List of executed SimulationTicks
        """
        target_ticks = int(seconds * self.TARGET_TICK_RATE)
        return self.run_ticks(target_ticks)

    def get_metrics(self) -> Dict:
        """Get simulation performance metrics.

        Returns:
            Dictionary of metrics including tick rate and timing
        """
        if not self.tick_history:
            return {
                "tick_count": 0,
                "avg_tick_rate": 0.0,
                "avg_delta_time": 0.0,
                "target_tick_rate": self.TARGET_TICK_RATE,
            }

        recent_ticks = self.tick_history[-100:]  # Last 100 ticks
        deltas = [t.delta_time for t in recent_ticks if t.delta_time > 0]

        avg_delta = sum(deltas) / len(deltas) if deltas else 0.0
        avg_rate = 1.0 / avg_delta if avg_delta > 0 else 0.0

        return {
            "tick_count": self.tick_count,
            "avg_tick_rate": round(avg_rate, 2),
            "avg_delta_time": round(avg_delta * 1000, 3),  # in ms
            "target_tick_rate": self.TARGET_TICK_RATE,
            "target_delta_ms": round(self.TARGET_TICK_DURATION * 1000, 3),
        }

    def initiate_access(self, initiator: str, responder: str) -> HandshakeSession:
        """Initiate an access request with double-handshake.

        Args:
            initiator: Requesting party identity
            responder: Target party identity

        Returns:
            HandshakeSession for the access request
        """
        return self.handshake_protocol.initiate_handshake(initiator, responder)

    def complete_access(
        self, session_id: str, confirmation_nonce: str
    ) -> HandshakeSession | None:
        """Complete an access request.

        Args:
            session_id: Session to complete
            confirmation_nonce: Confirmation nonce

        Returns:
            Updated session or None
        """
        # First respond to handshake
        session = self.handshake_protocol.respond_handshake(session_id)
        if session is None or session.state != HandshakeState.AWAITING_CONFIRMATION:
            return session

        # Then confirm
        return self.handshake_protocol.confirm_handshake(session_id, confirmation_nonce)


# Global engine instance
_engine: SimulationEngine | None = None


def get_engine() -> SimulationEngine:
    """Get or create the global simulation engine.

    Returns:
        The global SimulationEngine instance
    """
    global _engine
    if _engine is None:
        _engine = SimulationEngine()
    return _engine


__all__ = [
    "HandshakeState",
    "HandshakeSession",
    "SimulationTick",
    "DoubleHandshakeProtocol",
    "SimulationEngine",
    "get_engine",
]
