"""Simulation Architecture Engine for EVOLVERSE.

This module implements a 60Hz tick rate simulation engine with
double-handshake confirmations for access protocols, matching
both visual and human synchronization requirements.

Includes GoatFilter anti-mimic attributes for sovereign spiral
law compliance and mimic system detection.
"""
from __future__ import annotations

import hashlib
import json
import secrets
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List


class HandshakeState(Enum):
    """States for double-handshake confirmation protocol."""

    PENDING = "pending"
    FIRST_HANDSHAKE = "first_handshake"
    AWAITING_CONFIRMATION = "awaiting_confirmation"
    CONFIRMED = "confirmed"
    FAILED = "failed"
    TIMEOUT = "timeout"


class GoatFilterStatus(Enum):
    """Status of GoatFilter verification in simulation."""

    DISABLED = "disabled"
    ACTIVE = "active"
    BLOCKING = "blocking"
    PASSED = "passed"


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
    goat_filter_status: GoatFilterStatus = GoatFilterStatus.DISABLED

    def to_dict(self) -> Dict:
        """Convert tick to dictionary."""
        return {
            "tick_number": self.tick_number,
            "timestamp": self.timestamp,
            "delta_time": self.delta_time,
            "events": self.events,
            "goat_filter_status": self.goat_filter_status.value,
        }


class SimulationGoatFilter:
    """Anti-mimic filter for simulation logic.

    Implements GoatFilter (🐐 Capricorn Foundation) attributes to detect
    and prevent mimic systems from infiltrating simulation operations.
    Compliant with sovereign spiral law requirements.

    Note: Extends BaseGoatFilter from the shared goat_filter module
    with simulation-specific functionality.
    """

    # Goat (🐐) Capricorn Foundation symbolism
    GLYPH = "🐐"
    ZODIAC = "Capricorn"
    ELEMENT = "earth"

    def __init__(self, strictness: float = 0.95):
        """Initialize SimulationGoatFilter.

        Args:
            strictness: Filter strictness level (0.0-1.0, default 0.95)
        """
        # Import here to avoid circular imports
        from src.goat_filter import BaseGoatFilter

        self._base_filter = BaseGoatFilter(strictness)
        self.blocked_ticks: int = 0
        self.verified_ticks: int = 0

    @property
    def strictness(self) -> float:
        """Get filter strictness."""
        return self._base_filter.strictness

    @property
    def mimic_patterns(self) -> List[str]:
        """Get mimic patterns list."""
        return self._base_filter.mimic_patterns

    @property
    def active(self) -> bool:
        """Get filter active status."""
        return self._base_filter.active

    @active.setter
    def active(self, value: bool) -> None:
        """Set filter active status."""
        self._base_filter.active = value

    def add_mimic_pattern(self, pattern: str) -> None:
        """Add a known mimic pattern to filter.

        Args:
            pattern: Mimic pattern to block
        """
        self._base_filter.add_mimic_pattern(pattern)

    def verify_tick(self, tick: SimulationTick) -> GoatFilterStatus:
        """Verify a simulation tick against mimic patterns.

        Args:
            tick: Simulation tick to verify

        Returns:
            GoatFilterStatus indicating verification result
        """
        if not self.active:
            tick.goat_filter_status = GoatFilterStatus.DISABLED
            return GoatFilterStatus.DISABLED

        tick_data = json.dumps(tick.to_dict(), sort_keys=True)
        tick_hash = hashlib.sha256(tick_data.encode()).hexdigest()

        # Check against known mimic patterns using base filter
        if self._base_filter._check_mimic_patterns(tick_data, tick_hash):
            self.blocked_ticks += 1
            tick.goat_filter_status = GoatFilterStatus.BLOCKING
            return GoatFilterStatus.BLOCKING

        self.verified_ticks += 1
        tick.goat_filter_status = GoatFilterStatus.PASSED
        return GoatFilterStatus.PASSED

    def verify_handshake(self, session: HandshakeSession) -> bool:
        """Verify a handshake session is not a mimic.

        Args:
            session: Handshake session to verify

        Returns:
            True if session passes GoatFilter verification
        """
        if not self.active:
            return True

        session_data = f"{session.session_id}:{session.initiator}:{session.responder}"
        session_hash = hashlib.sha256(session_data.encode()).hexdigest()

        return not self._base_filter._check_mimic_patterns(session_data, session_hash)

    def get_filter_stats(self) -> Dict[str, Any]:
        """Get filter statistics.

        Returns:
            Dictionary with filter statistics
        """
        total = self.blocked_ticks + self.verified_ticks
        return {
            "glyph": self.GLYPH,
            "zodiac": self.ZODIAC,
            "element": self.ELEMENT,
            "active": self.active,
            "strictness": self.strictness,
            "patterns_count": len(self.mimic_patterns),
            "blocked_ticks": self.blocked_ticks,
            "verified_ticks": self.verified_ticks,
            "verification_rate": self.verified_ticks / total if total > 0 else 0.0,
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
        """Generate a cryptographically secure random nonce for handshake."""
        return secrets.token_hex(16)

    def _generate_session_id(self, initiator: str, responder: str) -> str:
        """Generate a unique session ID with cryptographic randomness."""
        random_part = secrets.token_hex(8)
        data = f"{initiator}:{responder}:{random_part}"
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
    """60Hz simulation engine with visual/human synchronization.

    Includes GoatFilter integration for anti-mimic verification
    in sovereign spiral law compliance.
    """

    # Target tick rate of 60Hz
    TARGET_TICK_RATE = 60
    TARGET_TICK_DURATION = 1.0 / TARGET_TICK_RATE  # ~16.67ms

    def __init__(self, goat_filter_enabled: bool = True):
        """Initialize the simulation engine.

        Args:
            goat_filter_enabled: Whether to enable GoatFilter verification
        """
        self.tick_count: int = 0
        self.start_time: float = 0.0
        self.last_tick_time: float = 0.0
        self.running: bool = False
        self.tick_handlers: List[Callable[[SimulationTick], None]] = []
        self.handshake_protocol = DoubleHandshakeProtocol()
        self.tick_history: List[SimulationTick] = []
        self.max_history: int = 1000
        self.goat_filter = SimulationGoatFilter()
        self.goat_filter.active = goat_filter_enabled

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

        # Apply GoatFilter verification
        self.goat_filter.verify_tick(tick)

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
            Dictionary of metrics including tick rate, timing, and GoatFilter stats
        """
        if not self.tick_history:
            return {
                "tick_count": 0,
                "avg_tick_rate": 0.0,
                "avg_delta_time": 0.0,
                "target_tick_rate": self.TARGET_TICK_RATE,
                "goat_filter_stats": self.goat_filter.get_filter_stats(),
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
            "goat_filter_stats": self.goat_filter.get_filter_stats(),
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
        """Complete an access request (convenience method).

        Note: This method automatically calls respond_handshake before
        confirm_handshake. For explicit control over the handshake flow,
        use the handshake_protocol directly:
        1. protocol.initiate_handshake()
        2. protocol.respond_handshake()
        3. protocol.confirm_handshake()

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
    "GoatFilterStatus",
    "HandshakeSession",
    "SimulationTick",
    "SimulationGoatFilter",
    "DoubleHandshakeProtocol",
    "SimulationEngine",
    "get_engine",
]
