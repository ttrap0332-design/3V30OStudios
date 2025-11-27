// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RippleEffect
 * @dev The 5-axis Ripple Effect forensic engine - sovereign physics of propagation,
 * extraction detection, proof-of-origin, and cycle control
 * 
 * This contract implements the XX/YY/ZZ/TT/WW matrix for on-chain ripple recording,
 * verification, and tribunal-ready proof generation.
 */
contract RippleEffect {
    
    // ============ STATE VARIABLES ============
    
    struct RippleVectorXX {
        bool detectedAlteration;
        string[] alterationTypes;
        bytes signature;
        address[] actors;
        uint256[] actorTimestamps;
    }
    
    struct RippleVectorYY {
        address currentOwner;
        address originalOwner;
        address[] returnPath;
        string restitutionStatus; // "pending", "in_progress", "completed", "blocked"
        uint256 stolenCyclesReturned;
    }
    
    struct RippleVectorZZ {
        uint256 scanDepth;
        uint256 hiddenContractsFound;
        uint256 ghostNodesFound;
        address[] hiddenLayers;
        string[] layerTypes;
        bool chainTheftDetected;
    }
    
    struct RippleVectorTT {
        uint256[] timestamps;
        string[] eventTypes;
        uint256[] intervals;
        string[] predictedCycles;
        string memoryWeave;
        bytes32 memoryHash;
    }
    
    struct RippleVectorWW {
        string realMotive;
        string statedReason;
        bool motiveMatch;
        string hiddenAgenda;
        address[] authorityChain;
        string psychologicalPattern;
        string orderBehindAction;
    }
    
    struct RippleEvent {
        string eventId;
        uint256 timestamp;
        string originShard;
        address contractAddress;
        string umbrella; // "SORA", "BLEU", "COSMIC", "CIVILIAN", "MILITARY"
        RippleVectorXX xx;
        RippleVectorYY yy;
        RippleVectorZZ zz;
        RippleVectorTT tt;
        RippleVectorWW ww;
        string[] effects;
        uint256 densityScore;
        string watchtowerEntry;
        string pulseArchiveRef;
        bytes32 proofHash;
        address[] witnesses;
        bool tribunalReady;
    }
    
    // ============ STORAGE ============
    
    mapping(string => RippleEvent) public rippleEvents;
    mapping(address => string[]) public shardRipples;
    mapping(string => bool) public eventExists;
    
    string[] public allEventIds;
    
    address public owner;
    address public watchtower;
    address public pulseArchive;
    
    // ============ EVENTS ============
    
    event RippleActivated(
        string indexed eventId,
        string originShard,
        address indexed contractAddress,
        uint256 timestamp
    );
    
    event TheftDetected(
        string indexed eventId,
        string[] alterationTypes,
        address[] actors
    );
    
    event ReturnInitiated(
        string indexed eventId,
        address originalOwner,
        uint256 stolenCycles
    );
    
    event HiddenLayerDiscovered(
        string indexed eventId,
        address hiddenContract,
        string layerType
    );
    
    event TribunalProofGenerated(
        string indexed eventId,
        bytes32 proofHash,
        address[] witnesses
    );
    
    // ============ MODIFIERS ============
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }
    
    modifier onlyWatchtower() {
        require(msg.sender == watchtower || msg.sender == owner, "Not watchtower");
        _;
    }
    
    // ============ CONSTRUCTOR ============
    
    constructor(address _watchtower, address _pulseArchive) {
        owner = msg.sender;
        watchtower = _watchtower;
        pulseArchive = _pulseArchive;
    }
    
    // ============ CORE FUNCTIONS ============
    
    /**
     * @dev Generate a new ripple event with all five vectors
     */
    function generateRipple(
        string memory _eventId,
        string memory _originShard,
        address _contractAddress,
        string memory _umbrella
    ) public returns (bool) {
        require(!eventExists[_eventId], "Event already exists");
        require(_contractAddress != address(0), "Invalid contract address");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        ripple.eventId = _eventId;
        ripple.timestamp = block.timestamp;
        ripple.originShard = _originShard;
        ripple.contractAddress = _contractAddress;
        ripple.umbrella = _umbrella;
        ripple.densityScore = 0;
        ripple.tribunalReady = false;
        
        // Initialize vectors with default values
        ripple.xx.detectedAlteration = false;
        ripple.yy.currentOwner = msg.sender;
        ripple.yy.originalOwner = msg.sender;
        ripple.yy.restitutionStatus = "completed";
        ripple.zz.scanDepth = 0;
        ripple.zz.chainTheftDetected = false;
        ripple.ww.motiveMatch = true;
        
        // Add timestamp to TT vector
        ripple.tt.timestamps.push(block.timestamp);
        ripple.tt.eventTypes.push("activation");
        ripple.tt.intervals.push(0);
        
        eventExists[_eventId] = true;
        allEventIds.push(_eventId);
        shardRipples[_contractAddress].push(_eventId);
        
        emit RippleActivated(_eventId, _originShard, _contractAddress, block.timestamp);
        
        return true;
    }
    
    /**
     * @dev Record XX Vector (The Cut) - alteration detection
     */
    function recordXXVector(
        string memory _eventId,
        bool _detectedAlteration,
        string[] memory _alterationTypes,
        address[] memory _actors
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        ripple.xx.detectedAlteration = _detectedAlteration;
        ripple.xx.alterationTypes = _alterationTypes;
        ripple.xx.actors = _actors;
        
        // Record timestamps for each actor
        for (uint i = 0; i < _actors.length; i++) {
            ripple.xx.actorTimestamps.push(block.timestamp);
        }
        
        if (_detectedAlteration) {
            emit TheftDetected(_eventId, _alterationTypes, _actors);
        }
        
        return true;
    }
    
    /**
     * @dev Record YY Vector (The Return) - return to source
     */
    function recordYYVector(
        string memory _eventId,
        address _originalOwner,
        address[] memory _returnPath,
        string memory _restitutionStatus,
        uint256 _stolenCyclesReturned
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        ripple.yy.originalOwner = _originalOwner;
        ripple.yy.returnPath = _returnPath;
        ripple.yy.restitutionStatus = _restitutionStatus;
        ripple.yy.stolenCyclesReturned = _stolenCyclesReturned;
        
        if (_stolenCyclesReturned > 0) {
            emit ReturnInitiated(_eventId, _originalOwner, _stolenCyclesReturned);
        }
        
        return true;
    }
    
    /**
     * @dev Record ZZ Vector (The Depth) - hidden layer detection
     */
    function recordZZVector(
        string memory _eventId,
        uint256 _scanDepth,
        address[] memory _hiddenLayers,
        string[] memory _layerTypes,
        bool _chainTheftDetected
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        require(_hiddenLayers.length == _layerTypes.length, "Array length mismatch");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        ripple.zz.scanDepth = _scanDepth;
        ripple.zz.hiddenContractsFound = _hiddenLayers.length;
        ripple.zz.hiddenLayers = _hiddenLayers;
        ripple.zz.layerTypes = _layerTypes;
        ripple.zz.chainTheftDetected = _chainTheftDetected;
        
        for (uint i = 0; i < _hiddenLayers.length; i++) {
            emit HiddenLayerDiscovered(_eventId, _hiddenLayers[i], _layerTypes[i]);
        }
        
        return true;
    }
    
    /**
     * @dev Record TT Vector (The Time) - temporal tracking
     */
    function recordTTVector(
        string memory _eventId,
        string memory _eventType,
        string memory _memoryWeave,
        bytes32 _memoryHash
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        uint256 lastTimestamp = ripple.tt.timestamps.length > 0 
            ? ripple.tt.timestamps[ripple.tt.timestamps.length - 1] 
            : block.timestamp;
        
        uint256 interval = block.timestamp - lastTimestamp;
        
        ripple.tt.timestamps.push(block.timestamp);
        ripple.tt.eventTypes.push(_eventType);
        ripple.tt.intervals.push(interval);
        ripple.tt.memoryWeave = _memoryWeave;
        ripple.tt.memoryHash = _memoryHash;
        
        return true;
    }
    
    /**
     * @dev Record WW Vector (The Intent) - motive and authority
     */
    function recordWWVector(
        string memory _eventId,
        string memory _realMotive,
        string memory _statedReason,
        string memory _hiddenAgenda,
        address[] memory _authorityChain,
        string memory _orderBehindAction
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        ripple.ww.realMotive = _realMotive;
        ripple.ww.statedReason = _statedReason;
        ripple.ww.motiveMatch = keccak256(bytes(_realMotive)) == keccak256(bytes(_statedReason));
        ripple.ww.hiddenAgenda = _hiddenAgenda;
        ripple.ww.authorityChain = _authorityChain;
        ripple.ww.orderBehindAction = _orderBehindAction;
        
        return true;
    }
    
    /**
     * @dev Update density score based on ripple impact
     */
    function updateDensityScore(
        string memory _eventId,
        uint256 _score
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        require(_score <= 100, "Score must be <= 100");
        
        rippleEvents[_eventId].densityScore = _score;
        return true;
    }
    
    /**
     * @dev Generate tribunal-ready proof
     */
    function generateTribunalProof(
        string memory _eventId,
        bytes32 _proofHash,
        address[] memory _witnesses
    ) public onlyWatchtower returns (bool) {
        require(eventExists[_eventId], "Event does not exist");
        require(_witnesses.length >= 3, "Minimum 3 witnesses required");
        
        RippleEvent storage ripple = rippleEvents[_eventId];
        
        ripple.proofHash = _proofHash;
        ripple.witnesses = _witnesses;
        ripple.tribunalReady = true;
        
        emit TribunalProofGenerated(_eventId, _proofHash, _witnesses);
        
        return true;
    }
    
    // ============ VIEW FUNCTIONS ============
    
    /**
     * @dev Get complete ripple event data
     */
    function getRippleEvent(string memory _eventId) 
        public 
        view 
        returns (RippleEvent memory) 
    {
        require(eventExists[_eventId], "Event does not exist");
        return rippleEvents[_eventId];
    }
    
    /**
     * @dev Get all ripple events for a shard
     */
    function getShardRipples(address _shardAddress) 
        public 
        view 
        returns (string[] memory) 
    {
        return shardRipples[_shardAddress];
    }
    
    /**
     * @dev Check if theft detected in XX vector
     */
    function isTheftDetected(string memory _eventId) 
        public 
        view 
        returns (bool) 
    {
        require(eventExists[_eventId], "Event does not exist");
        return rippleEvents[_eventId].xx.detectedAlteration;
    }
    
    /**
     * @dev Get restitution status from YY vector
     */
    function getRestitutionStatus(string memory _eventId) 
        public 
        view 
        returns (string memory, uint256) 
    {
        require(eventExists[_eventId], "Event does not exist");
        RippleEvent memory ripple = rippleEvents[_eventId];
        return (ripple.yy.restitutionStatus, ripple.yy.stolenCyclesReturned);
    }
    
    /**
     * @dev Check if chain theft detected in ZZ vector
     */
    function isChainTheftDetected(string memory _eventId) 
        public 
        view 
        returns (bool) 
    {
        require(eventExists[_eventId], "Event does not exist");
        return rippleEvents[_eventId].zz.chainTheftDetected;
    }
    
    /**
     * @dev Get temporal log from TT vector
     */
    function getTemporalLog(string memory _eventId) 
        public 
        view 
        returns (uint256[] memory, string[] memory, uint256[] memory) 
    {
        require(eventExists[_eventId], "Event does not exist");
        RippleEvent memory ripple = rippleEvents[_eventId];
        return (ripple.tt.timestamps, ripple.tt.eventTypes, ripple.tt.intervals);
    }
    
    /**
     * @dev Check if motive matches stated reason in WW vector
     */
    function isMotiveMatch(string memory _eventId) 
        public 
        view 
        returns (bool) 
    {
        require(eventExists[_eventId], "Event does not exist");
        return rippleEvents[_eventId].ww.motiveMatch;
    }
    
    /**
     * @dev Get tribunal proof status
     */
    function getTribunalProof(string memory _eventId) 
        public 
        view 
        returns (bytes32, address[] memory, bool) 
    {
        require(eventExists[_eventId], "Event does not exist");
        RippleEvent memory ripple = rippleEvents[_eventId];
        return (ripple.proofHash, ripple.witnesses, ripple.tribunalReady);
    }
    
    /**
     * @dev Get total number of ripple events
     */
    function getTotalEvents() public view returns (uint256) {
        return allEventIds.length;
    }
    
    // ============ ADMIN FUNCTIONS ============
    
    function setWatchtower(address _watchtower) public onlyOwner {
        watchtower = _watchtower;
    }
    
    function setPulseArchive(address _pulseArchive) public onlyOwner {
        pulseArchive = _pulseArchive;
    }
    
    function transferOwnership(address _newOwner) public onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
}
