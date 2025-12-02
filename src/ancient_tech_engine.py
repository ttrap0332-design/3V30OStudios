"""Ancient Technologies Engine for EVOLVERSE Integration.

This module provides integration components for adapting ancient technologies,
texts, and archaeological discoveries into EV0L's military, medical, and
economic paradigms. Implements pyramid muon imaging, Hebrew gematria encoding,
Indus seal blockchain prototypes, and stress corridor laboratory systems.
"""
from __future__ import annotations

import hashlib
import json
import secrets
import time
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional


class PyramidVoidClassification(Enum):
    """Classification types for detected pyramid voids.

    Used to categorize voids discovered via muon tomography based on
    their strategic value for EVOLVERSE integration.
    """

    ATOMIC_ENGINE_HUB = "atomic_engine_hub"
    HIDDEN_CHAMBER_LAB = "hidden_chamber_lab"
    STORAGE_VAULT = "storage_vault"
    ENERGY_CONDUIT = "energy_conduit"
    UNCLASSIFIED = "unclassified"


class LaborTokenTier(Enum):
    """Tier classifications for Indus-style labor tokens.

    Defines skill levels for workforce validation tokens based on
    ancient Indus Valley seal hierarchies.
    """

    APPRENTICE = "apprentice"
    JOURNEYMAN = "journeyman"
    MASTER = "master"
    SOVEREIGN = "sovereign"


class HealingFrequency(Enum):
    """Solfeggio healing frequencies aligned with Hebrew gematria.

    Maps ancient Solfeggio frequencies to healing functions,
    integrated with gematria encoding for pharmaceutical and sonic systems.
    """

    LIBERATION = 396
    TRANSFORMATION = 417
    DNA_REPAIR = 528
    CONNECTION = 639
    AWAKENING = 741
    INTUITION = 852
    DIVINE_LIGHT = 963


# Hebrew letter to gematria value mapping
HEBREW_GEMATRIA: Dict[str, int] = {
    "א": 1,  # Aleph
    "ב": 2,  # Bet
    "ג": 3,  # Gimel
    "ד": 4,  # Dalet
    "ה": 5,  # He
    "ו": 6,  # Vav
    "ז": 7,  # Zayin
    "ח": 8,  # Chet
    "ט": 9,  # Tet
    "י": 10,  # Yod
    "כ": 20,  # Kaf
    "ל": 30,  # Lamed
    "מ": 40,  # Mem
    "נ": 50,  # Nun
    "ס": 60,  # Samekh
    "ע": 70,  # Ayin
    "פ": 80,  # Pe
    "צ": 90,  # Tsade
    "ק": 100,  # Qof
    "ר": 200,  # Resh
    "ש": 300,  # Shin
    "ת": 400,  # Tav
}


@dataclass
class PyramidVoid:
    """Represents a detected void within a pyramid structure.

    Attributes:
        void_id: Unique identifier for the void
        volume_cubic_meters: Volume of the detected void
        depth_meters: Depth from pyramid surface
        classification: Type classification of the void
        shielding_factor: Natural radiation shielding effectiveness (0-1)
        integration_status: Current status of EVOLVERSE integration
    """

    void_id: str
    volume_cubic_meters: float
    depth_meters: float
    classification: PyramidVoidClassification
    shielding_factor: float
    integration_status: str = "surveyed"
    detected_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary containing void data
        """
        return {
            "void_id": self.void_id,
            "volume_cubic_meters": self.volume_cubic_meters,
            "depth_meters": self.depth_meters,
            "classification": self.classification.value,
            "shielding_factor": self.shielding_factor,
            "integration_status": self.integration_status,
            "detected_at": self.detected_at,
            "detected_at_iso": datetime.fromtimestamp(self.detected_at).isoformat(),
        }


@dataclass
class PyramidSurvey:
    """Represents a complete pyramid muon imaging survey.

    Attributes:
        pyramid_id: Unique identifier for the pyramid
        location_name: Geographic location name
        location_glyph: Ceremonial glyph for the location
        detected_voids: List of detected voids
        survey_duration_days: Duration of muon exposure
        covenant_seal: Ceremonial seal of authentication
    """

    pyramid_id: str
    location_name: str
    location_glyph: str = "⛛"
    detected_voids: List[PyramidVoid] = field(default_factory=list)
    survey_duration_days: int = 30
    covenant_seal: str = "♈️♈️🐏🐏"
    survey_start: float = field(default_factory=time.time)

    def add_void(self, void: PyramidVoid) -> None:
        """Add a detected void to the survey.

        Args:
            void: The PyramidVoid to add
        """
        self.detected_voids.append(void)

    def get_total_void_volume(self) -> float:
        """Calculate total volume of all detected voids.

        Returns:
            Total volume in cubic meters
        """
        return sum(v.volume_cubic_meters for v in self.detected_voids)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary containing survey data
        """
        return {
            "pyramid_id": self.pyramid_id,
            "location_name": self.location_name,
            "location_glyph": self.location_glyph,
            "detected_voids": [v.to_dict() for v in self.detected_voids],
            "survey_duration_days": self.survey_duration_days,
            "covenant_seal": self.covenant_seal,
            "survey_start": self.survey_start,
            "survey_start_iso": datetime.fromtimestamp(self.survey_start).isoformat(),
            "total_void_volume": self.get_total_void_volume(),
            "void_count": len(self.detected_voids),
        }


class PyramidMuonImaging:
    """Handles pyramid void detection via muon tomography.

    Implements the survey, detection, and classification of pyramid voids
    for integration as atomic-engine hubs or hidden-chamber labs.
    """

    # Classification thresholds
    ATOMIC_HUB_MIN_VOLUME = 200  # cubic meters
    ATOMIC_HUB_MIN_SHIELDING = 0.95
    CHAMBER_LAB_MIN_VOLUME = 100  # cubic meters
    CHAMBER_LAB_MIN_DEPTH = 20  # meters
    STORAGE_VAULT_MIN_VOLUME = 50  # cubic meters
    ENERGY_CONDUIT_MIN_VOLUME = 10  # cubic meters
    DEFAULT_SURVEY_DURATION = 30  # days

    def __init__(self, output_dir: str | Path = "data/pyramid_surveys"):
        """Initialize the muon imaging system.

        Args:
            output_dir: Directory for survey output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.surveys: Dict[str, PyramidSurvey] = {}

    def _generate_void_id(self) -> str:
        """Generate a unique void identifier.

        Returns:
            Unique void ID string
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"V-{timestamp}-{random_suffix}"

    def _generate_pyramid_id(self, location_name: str) -> str:
        """Generate a unique pyramid identifier.

        Args:
            location_name: Name of the pyramid location

        Returns:
            Unique pyramid ID string
        """
        name_hash = hashlib.sha256(location_name.encode()).hexdigest()[:8]
        return f"PYR-{name_hash}"

    def create_survey(
        self,
        location_name: str,
        survey_duration_days: int = 30,
        location_glyph: str = "⛛",
    ) -> PyramidSurvey:
        """Create a new pyramid survey.

        Args:
            location_name: Geographic location name
            survey_duration_days: Duration of muon exposure
            location_glyph: Ceremonial glyph for location

        Returns:
            Created PyramidSurvey instance
        """
        pyramid_id = self._generate_pyramid_id(location_name)
        survey = PyramidSurvey(
            pyramid_id=pyramid_id,
            location_name=location_name,
            location_glyph=location_glyph,
            survey_duration_days=survey_duration_days,
        )
        self.surveys[pyramid_id] = survey
        return survey

    def detect_void(
        self,
        survey: PyramidSurvey,
        volume_cubic_meters: float,
        depth_meters: float,
        classification: PyramidVoidClassification = PyramidVoidClassification.UNCLASSIFIED,
        shielding_factor: float = 0.9,
    ) -> PyramidVoid:
        """Detect and record a void in a pyramid survey.

        Args:
            survey: The PyramidSurvey to add the void to
            volume_cubic_meters: Volume of the detected void
            depth_meters: Depth from pyramid surface
            classification: Type classification of the void
            shielding_factor: Natural shielding effectiveness

        Returns:
            Created PyramidVoid instance
        """
        void = PyramidVoid(
            void_id=self._generate_void_id(),
            volume_cubic_meters=volume_cubic_meters,
            depth_meters=depth_meters,
            classification=classification,
            shielding_factor=shielding_factor,
        )
        survey.add_void(void)
        return void

    def classify_void_for_integration(
        self, void: PyramidVoid
    ) -> PyramidVoidClassification:
        """Classify a void for EVOLVERSE integration.

        Uses volume and depth to determine optimal use.

        Args:
            void: The void to classify

        Returns:
            Classification for the void
        """
        if (void.volume_cubic_meters >= self.ATOMIC_HUB_MIN_VOLUME 
                and void.shielding_factor >= self.ATOMIC_HUB_MIN_SHIELDING):
            return PyramidVoidClassification.ATOMIC_ENGINE_HUB
        elif (void.volume_cubic_meters >= self.CHAMBER_LAB_MIN_VOLUME 
                and void.depth_meters >= self.CHAMBER_LAB_MIN_DEPTH):
            return PyramidVoidClassification.HIDDEN_CHAMBER_LAB
        elif void.volume_cubic_meters >= self.STORAGE_VAULT_MIN_VOLUME:
            return PyramidVoidClassification.STORAGE_VAULT
        elif void.volume_cubic_meters >= self.ENERGY_CONDUIT_MIN_VOLUME:
            return PyramidVoidClassification.ENERGY_CONDUIT
        return PyramidVoidClassification.UNCLASSIFIED

    def export_survey(self, pyramid_id: str, filename: str | None = None) -> Path:
        """Export a survey to JSON file.

        Args:
            pyramid_id: ID of the pyramid survey to export
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file

        Raises:
            KeyError: If pyramid_id not found
        """
        survey = self.surveys.get(pyramid_id)
        if survey is None:
            raise KeyError(f"Survey not found: {pyramid_id}")

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"pyramid_survey_{pyramid_id}_{timestamp}.json"

        filepath = self.output_dir / filename
        with filepath.open("w", encoding="utf-8") as f:
            json.dump(survey.to_dict(), f, indent=2)

        return filepath


@dataclass
class GematriaFormula:
    """Represents a gematria-encoded formula.

    Attributes:
        formula_id: Unique identifier
        hebrew_name: Name in Hebrew letters
        gematria_value: Computed gematria sum
        sonic_frequency: Associated healing frequency
        pharmaceutical_class: Classification for medical use
    """

    formula_id: str
    hebrew_name: str
    gematria_value: int
    sonic_frequency: int
    pharmaceutical_class: str
    created_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary containing formula data
        """
        return {
            "formula_id": self.formula_id,
            "hebrew_name": self.hebrew_name,
            "gematria_value": self.gematria_value,
            "sonic_frequency": self.sonic_frequency,
            "pharmaceutical_class": self.pharmaceutical_class,
            "created_at": self.created_at,
            "created_at_iso": datetime.fromtimestamp(self.created_at).isoformat(),
        }


class HebrewGematriaEncoder:
    """Encodes and decodes using Hebrew gematria system.

    Implements glyph-coded pharmaceutical formulas and EL0V8 integration
    with sonic encryption and healing frequency systems.
    """

    # Frequency to pharmaceutical class mapping
    FREQUENCY_CLASSES: Dict[int, str] = {
        396: "Liberation/Root",
        417: "Transformation",
        528: "DNA Repair",
        639: "Connection",
        741: "Awakening",
        852: "Intuition",
        963: "Divine Light",
    }

    # Number of harmonics to generate (aligned with Hebrew letter count)
    HARMONIC_COUNT = 7

    def __init__(self, output_dir: str | Path = "data/gematria_formulas"):
        """Initialize the gematria encoder.

        Args:
            output_dir: Directory for formula output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.formulas: Dict[str, GematriaFormula] = {}

    def calculate_gematria(self, hebrew_text: str) -> int:
        """Calculate the gematria value of Hebrew text.

        Args:
            hebrew_text: Hebrew letters to calculate

        Returns:
            Sum of gematria values
        """
        total = 0
        for char in hebrew_text:
            if char in HEBREW_GEMATRIA:
                total += HEBREW_GEMATRIA[char]
        return total

    def _generate_formula_id(self, hebrew_name: str) -> str:
        """Generate a unique formula identifier.

        Args:
            hebrew_name: Hebrew name of the formula

        Returns:
            Unique formula ID string
        """
        name_hash = hashlib.sha256(hebrew_name.encode()).hexdigest()[:8]
        return f"GEM-{name_hash}"

    def map_to_frequency(self, gematria_value: int) -> int:
        """Map a gematria value to a healing frequency.

        Uses modular arithmetic to map any gematria value to
        one of the Solfeggio frequencies.

        Args:
            gematria_value: The gematria sum to map

        Returns:
            Corresponding healing frequency in Hz
        """
        frequencies = list(HealingFrequency)
        index = gematria_value % len(frequencies)
        return frequencies[index].value

    def create_formula(
        self,
        hebrew_name: str,
        pharmaceutical_class: Optional[str] = None,
    ) -> GematriaFormula:
        """Create a gematria-encoded formula.

        Args:
            hebrew_name: Name in Hebrew letters
            pharmaceutical_class: Optional classification override

        Returns:
            Created GematriaFormula instance
        """
        gematria_value = self.calculate_gematria(hebrew_name)
        sonic_frequency = self.map_to_frequency(gematria_value)

        if pharmaceutical_class is None:
            pharmaceutical_class = self.FREQUENCY_CLASSES.get(
                sonic_frequency, "General"
            )

        formula = GematriaFormula(
            formula_id=self._generate_formula_id(hebrew_name),
            hebrew_name=hebrew_name,
            gematria_value=gematria_value,
            sonic_frequency=sonic_frequency,
            pharmaceutical_class=pharmaceutical_class,
        )
        self.formulas[formula.formula_id] = formula
        return formula

    def encode_sonic_payload(self, data: str, hebrew_key: str) -> Dict[str, Any]:
        """Encode data as a sonic payload using gematria key.

        Args:
            data: Data to encode
            hebrew_key: Hebrew letters for encryption key

        Returns:
            Encoded sonic payload dictionary
        """
        key_value = self.calculate_gematria(hebrew_key)
        frequency = self.map_to_frequency(key_value)

        # Generate harmonic series aligned with Hebrew letter count
        harmonics = [frequency * (i + 1) for i in range(self.HARMONIC_COUNT)]

        # Create payload hash
        payload_data = f"{data}:{hebrew_key}:{key_value}:{time.time()}"
        payload_hash = hashlib.sha256(payload_data.encode()).hexdigest()

        return {
            "payload_hash": payload_hash,
            "base_frequency": frequency,
            "harmonics": harmonics,
            "gematria_key": key_value,
            "hebrew_seal": hebrew_key,
            "timestamp": time.time(),
            "encoding_type": "sonic_gematria",
        }

    def export_formulas(self, filename: str | None = None) -> Path:
        """Export all formulas to JSON file.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gematria_formulas_{timestamp}.json"

        filepath = self.output_dir / filename
        data = {
            "export_timestamp": time.time(),
            "formula_count": len(self.formulas),
            "formulas": [f.to_dict() for f in self.formulas.values()],
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return filepath


@dataclass
class IndusLaborToken:
    """Represents an Indus-style labor validation token.

    Attributes:
        token_id: Unique token identifier
        holder_name: Name of the token holder
        skill_class: Classification of labor skills
        tier: Token tier level
        dna_hash: Hash of biometric binding
        glyph_seal: Ceremonial seal verification
        vault_binding: Address of bound vault
    """

    token_id: str
    holder_name: str
    skill_class: str
    tier: LaborTokenTier
    dna_hash: str
    glyph_seal: str
    vault_binding: str = ""
    minted_at: float = field(default_factory=time.time)
    is_validated: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary containing token data
        """
        return {
            "token_id": self.token_id,
            "holder_name": self.holder_name,
            "skill_class": self.skill_class,
            "tier": self.tier.value,
            "dna_hash": self.dna_hash,
            "glyph_seal": self.glyph_seal,
            "vault_binding": self.vault_binding,
            "minted_at": self.minted_at,
            "minted_at_iso": datetime.fromtimestamp(self.minted_at).isoformat(),
            "is_validated": self.is_validated,
        }


class IndusSealBlockchain:
    """Implements Indus seal blockchain prototypes.

    Provides labor token minting, validation, and vault binding
    using DNA/glyph-secure ENFT protocols.
    """

    def __init__(self, output_dir: str | Path = "data/indus_tokens"):
        """Initialize the Indus seal blockchain.

        Args:
            output_dir: Directory for token output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.tokens: Dict[str, IndusLaborToken] = {}
        self.vault_registry: Dict[str, List[str]] = {}

    def _generate_token_id(self) -> str:
        """Generate a unique token identifier.

        Returns:
            Unique token ID string
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(4)
        return f"ILT-{timestamp}-{random_suffix}"

    def _compute_dna_hash(self, biometric_data: str) -> str:
        """Compute hash from biometric data.

        Args:
            biometric_data: Raw biometric identifier

        Returns:
            SHA-256 hash of the data
        """
        return hashlib.sha256(biometric_data.encode()).hexdigest()

    def mint_labor_token(
        self,
        holder_name: str,
        skill_class: str,
        biometric_data: str,
        glyph_seal: str,
        tier: LaborTokenTier = LaborTokenTier.APPRENTICE,
    ) -> IndusLaborToken:
        """Mint a new labor validation token.

        Args:
            holder_name: Name of the token holder
            skill_class: Classification of labor skills
            biometric_data: Biometric data for DNA binding
            glyph_seal: Ceremonial seal verification
            tier: Token tier level

        Returns:
            Created IndusLaborToken instance
        """
        token = IndusLaborToken(
            token_id=self._generate_token_id(),
            holder_name=holder_name,
            skill_class=skill_class,
            tier=tier,
            dna_hash=self._compute_dna_hash(biometric_data),
            glyph_seal=glyph_seal,
        )
        self.tokens[token.token_id] = token
        return token

    def validate_token(self, token_id: str, biometric_check: str) -> bool:
        """Validate a labor token against biometric data.

        Args:
            token_id: ID of the token to validate
            biometric_check: Biometric data to check against

        Returns:
            True if validation successful
        """
        token = self.tokens.get(token_id)
        if token is None:
            return False

        check_hash = self._compute_dna_hash(biometric_check)
        if check_hash == token.dna_hash:
            token.is_validated = True
            return True
        return False

    def bind_to_vault(self, token_id: str, vault_address: str) -> bool:
        """Bind a token to an economic vault.

        Args:
            token_id: ID of the token to bind
            vault_address: Address of the vault

        Returns:
            True if binding successful
        """
        token = self.tokens.get(token_id)
        if token is None or not token.is_validated:
            return False

        token.vault_binding = vault_address

        if vault_address not in self.vault_registry:
            self.vault_registry[vault_address] = []
        self.vault_registry[vault_address].append(token_id)

        return True

    def export_tokens(self, filename: str | None = None) -> Path:
        """Export all tokens to JSON file.

        Args:
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"indus_tokens_{timestamp}.json"

        filepath = self.output_dir / filename
        data = {
            "export_timestamp": time.time(),
            "token_count": len(self.tokens),
            "tokens": [t.to_dict() for t in self.tokens.values()],
            "vault_registry": self.vault_registry,
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return filepath


@dataclass
class StressCorridorReading:
    """Represents a sensor reading from the stress corridor lab.

    Attributes:
        reading_id: Unique reading identifier
        thermal_value: Temperature in Celsius
        pressure_value: Pressure in kPa
        purity_value: Purity percentage (0-100)
        timestamp: Time of reading
    """

    reading_id: str
    thermal_value: float
    pressure_value: float
    purity_value: float
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary containing reading data
        """
        return {
            "reading_id": self.reading_id,
            "thermal_value": self.thermal_value,
            "pressure_value": self.pressure_value,
            "purity_value": self.purity_value,
            "timestamp": self.timestamp,
            "timestamp_iso": datetime.fromtimestamp(self.timestamp).isoformat(),
        }


@dataclass
class LabSession:
    """Represents a stress corridor laboratory session.

    Attributes:
        session_id: Unique session identifier
        lab_type: Type of laboratory operation
        readings: List of sensor readings
        esoil_integration: E-SOIL atomic recursion status
    """

    session_id: str
    lab_type: str
    readings: List[StressCorridorReading] = field(default_factory=list)
    esoil_integration: bool = False
    started_at: float = field(default_factory=time.time)
    is_active: bool = True

    def add_reading(self, reading: StressCorridorReading) -> None:
        """Add a sensor reading to the session.

        Args:
            reading: The StressCorridorReading to add
        """
        self.readings.append(reading)

    def get_average_purity(self) -> float:
        """Calculate average purity across all readings.

        Returns:
            Average purity percentage
        """
        if not self.readings:
            return 0.0
        return sum(r.purity_value for r in self.readings) / len(self.readings)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary containing session data
        """
        return {
            "session_id": self.session_id,
            "lab_type": self.lab_type,
            "readings": [r.to_dict() for r in self.readings],
            "reading_count": len(self.readings),
            "average_purity": self.get_average_purity(),
            "esoil_integration": self.esoil_integration,
            "started_at": self.started_at,
            "started_at_iso": datetime.fromtimestamp(self.started_at).isoformat(),
            "is_active": self.is_active,
        }


class StressCorridorLab:
    """Implements stress corridor laboratory feedback systems.

    Provides adaptive geothermal filtration integrated with E-SOIL
    atomic recursions for environmental sustainability prototypes.
    """

    # E-SOIL feedback target values
    THERMAL_TARGET = 25.0  # Optimal temperature in Celsius
    PRESSURE_TARGET = 101.325  # Standard atmosphere in kPa
    PURITY_TARGET = 99.0  # Target purity percentage

    # Feedback adjustment factors
    THERMAL_ADJUSTMENT_FACTOR = 0.1
    PRESSURE_ADJUSTMENT_FACTOR = 0.05
    FLOW_ADJUSTMENT_FACTOR = 0.02

    # Lab type configurations
    LAB_TYPES: Dict[str, Dict[str, Any]] = {
        "GeoFilter-Alpha": {
            "function": "Groundwater purification",
            "esoil_integration": "Recursive mineral extraction",
        },
        "AtmoClean-Beta": {
            "function": "Air particulate removal",
            "esoil_integration": "Stress-gradient separation",
        },
        "ThermoHarvest-Gamma": {
            "function": "Geothermal energy capture",
            "esoil_integration": "Atomic recursion cycling",
        },
        "BioRemediate-Delta": {
            "function": "Soil decontamination",
            "esoil_integration": "Self-healing substrate",
        },
    }

    def __init__(self, output_dir: str | Path = "data/stress_corridor_labs"):
        """Initialize the stress corridor lab system.

        Args:
            output_dir: Directory for lab output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.sessions: Dict[str, LabSession] = {}

    def _generate_session_id(self, lab_type: str) -> str:
        """Generate a unique session identifier.

        Args:
            lab_type: Type of lab operation

        Returns:
            Unique session ID string
        """
        timestamp = int(time.time() * 1000)
        type_prefix = lab_type.split("-")[0][:4].upper()
        random_suffix = secrets.token_hex(2)
        return f"LAB-{type_prefix}-{timestamp}-{random_suffix}"

    def _generate_reading_id(self) -> str:
        """Generate a unique reading identifier.

        Returns:
            Unique reading ID string
        """
        timestamp = int(time.time() * 1000)
        random_suffix = secrets.token_hex(2)
        return f"RDG-{timestamp}-{random_suffix}"

    def start_session(
        self, lab_type: str, enable_esoil: bool = True
    ) -> LabSession:
        """Start a new laboratory session.

        Args:
            lab_type: Type of laboratory operation
            enable_esoil: Whether to enable E-SOIL integration

        Returns:
            Created LabSession instance
        """
        session = LabSession(
            session_id=self._generate_session_id(lab_type),
            lab_type=lab_type,
            esoil_integration=enable_esoil,
        )
        self.sessions[session.session_id] = session
        return session

    def record_reading(
        self,
        session: LabSession,
        thermal_value: float,
        pressure_value: float,
        purity_value: float,
    ) -> StressCorridorReading:
        """Record a sensor reading in a session.

        Args:
            session: The LabSession to record in
            thermal_value: Temperature reading
            pressure_value: Pressure reading
            purity_value: Purity percentage

        Returns:
            Created StressCorridorReading instance
        """
        reading = StressCorridorReading(
            reading_id=self._generate_reading_id(),
            thermal_value=thermal_value,
            pressure_value=pressure_value,
            purity_value=purity_value,
        )
        session.add_reading(reading)
        return reading

    def compute_feedback_adjustment(
        self, session: LabSession
    ) -> Dict[str, float]:
        """Compute adaptive feedback adjustments.

        Uses E-SOIL atomic recursion logic to determine
        optimal parameter adjustments.

        Args:
            session: The LabSession to analyze

        Returns:
            Dictionary of adjustment values
        """
        if not session.readings:
            return {"thermal_adj": 0.0, "pressure_adj": 0.0, "flow_adj": 0.0}

        # Get latest readings
        latest = session.readings[-1]

        # E-SOIL recursion logic using class constants
        thermal_adj = ((self.THERMAL_TARGET - latest.thermal_value) 
                       * self.THERMAL_ADJUSTMENT_FACTOR)
        pressure_adj = ((self.PRESSURE_TARGET - latest.pressure_value) 
                        * self.PRESSURE_ADJUSTMENT_FACTOR)
        flow_adj = ((self.PURITY_TARGET - latest.purity_value) 
                    * self.FLOW_ADJUSTMENT_FACTOR)

        return {
            "thermal_adj": round(thermal_adj, 4),
            "pressure_adj": round(pressure_adj, 4),
            "flow_adj": round(flow_adj, 4),
            "recursion_cycle": len(session.readings),
        }

    def end_session(self, session_id: str) -> bool:
        """End a laboratory session.

        Args:
            session_id: ID of the session to end

        Returns:
            True if session ended successfully
        """
        session = self.sessions.get(session_id)
        if session is None:
            return False

        session.is_active = False
        return True

    def export_session(self, session_id: str, filename: str | None = None) -> Path:
        """Export a session to JSON file.

        Args:
            session_id: ID of the session to export
            filename: Optional filename (auto-generated if None)

        Returns:
            Path to the exported file

        Raises:
            KeyError: If session_id not found
        """
        session = self.sessions.get(session_id)
        if session is None:
            raise KeyError(f"Session not found: {session_id}")

        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"lab_session_{session_id}_{timestamp}.json"

        filepath = self.output_dir / filename
        data = {
            "session": session.to_dict(),
            "lab_config": self.LAB_TYPES.get(session.lab_type, {}),
            "final_adjustment": self.compute_feedback_adjustment(session),
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return filepath


class AncientTechRegistry:
    """Central registry for all ancient technology integrations.

    Provides unified tracking and export of all ancient technology
    artifacts across pyramid imaging, gematria, Indus seals, and
    stress corridor laboratories.
    """

    def __init__(self, output_dir: str | Path = "data"):
        """Initialize the ancient tech registry.

        Args:
            output_dir: Root data directory
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize subsystems
        self.pyramid_imaging = PyramidMuonImaging(self.output_dir / "pyramid_surveys")
        self.gematria_encoder = HebrewGematriaEncoder(
            self.output_dir / "gematria_formulas"
        )
        self.indus_blockchain = IndusSealBlockchain(self.output_dir / "indus_tokens")
        self.stress_corridor = StressCorridorLab(
            self.output_dir / "stress_corridor_labs"
        )

    def export_full_registry(self, filename: str = "ancient_tech_registry.json") -> Path:
        """Export the complete registry to JSON.

        Args:
            filename: Output filename

        Returns:
            Path to the exported file
        """
        filepath = self.output_dir / filename
        data = {
            "export_timestamp": time.time(),
            "export_timestamp_iso": datetime.now().isoformat(),
            "covenant_seal": "⛛ℵॐ⟨⟩",
            "double_ram_seal": "♈️♈️🐏🐏",
            "subsystems": {
                "pyramid_imaging": {
                    "survey_count": len(self.pyramid_imaging.surveys),
                    "surveys": [
                        s.to_dict() for s in self.pyramid_imaging.surveys.values()
                    ],
                },
                "gematria_encoder": {
                    "formula_count": len(self.gematria_encoder.formulas),
                    "formulas": [
                        f.to_dict() for f in self.gematria_encoder.formulas.values()
                    ],
                },
                "indus_blockchain": {
                    "token_count": len(self.indus_blockchain.tokens),
                    "tokens": [
                        t.to_dict() for t in self.indus_blockchain.tokens.values()
                    ],
                    "vault_registry": self.indus_blockchain.vault_registry,
                },
                "stress_corridor": {
                    "session_count": len(self.stress_corridor.sessions),
                    "sessions": [
                        s.to_dict() for s in self.stress_corridor.sessions.values()
                    ],
                },
            },
        }

        with filepath.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return filepath


# Module-level convenience functions
_registry: AncientTechRegistry | None = None


def get_registry(output_dir: str | Path = "data") -> AncientTechRegistry:
    """Get or create the global ancient tech registry.

    Args:
        output_dir: Root data directory

    Returns:
        The global AncientTechRegistry instance
    """
    global _registry
    if _registry is None:
        _registry = AncientTechRegistry(output_dir)
    return _registry


__all__ = [
    "PyramidVoidClassification",
    "LaborTokenTier",
    "HealingFrequency",
    "HEBREW_GEMATRIA",
    "PyramidVoid",
    "PyramidSurvey",
    "PyramidMuonImaging",
    "GematriaFormula",
    "HebrewGematriaEncoder",
    "IndusLaborToken",
    "IndusSealBlockchain",
    "StressCorridorReading",
    "LabSession",
    "StressCorridorLab",
    "AncientTechRegistry",
    "get_registry",
]
