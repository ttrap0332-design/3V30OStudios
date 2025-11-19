import { ethers } from "hardhat";

/**
 * Deploy Ripple Effect Contract
 * 
 * This script deploys the RippleEffect smart contract with all 5 vectors
 * (XX, YY, ZZ, TT, WW) for on-chain ripple recording and verification.
 */
async function main() {
  console.log("🌊 Deploying Ripple Effect System...\n");

  const [deployer] = await ethers.getSigners();
  console.log("Deploying with account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString(), "\n");

  // Get contract factory
  const RippleEffect = await ethers.getContractFactory("RippleEffect");

  // Deploy with watchtower and pulse archive addresses
  // TODO: Replace with actual deployed addresses
  const watchtowerAddress = process.env.WATCHTOWER_ADDRESS || deployer.address;
  const pulseArchiveAddress = process.env.PULSE_ARCHIVE_ADDRESS || deployer.address;

  console.log("Watchtower address:", watchtowerAddress);
  console.log("Pulse Archive address:", pulseArchiveAddress);
  console.log("\nDeploying contract...");

  const rippleEffect = await RippleEffect.deploy(
    watchtowerAddress,
    pulseArchiveAddress
  );

  await rippleEffect.deployed();

  console.log("\n✅ RippleEffect deployed to:", rippleEffect.address);

  // Generate sample ripple event
  console.log("\n🔄 Generating sample ripple event...");

  const tx = await rippleEffect.generateRipple(
    "RIPPLE-2025-DEPLOY001",
    "Dimensional Spiral Port",
    "0x43dC17dF7919D25c06a01D52aAad94718C6bf87c",
    "SORA"
  );

  await tx.wait();
  console.log("✅ Sample ripple generated");

  // Get the ripple event
  const rippleEvent = await rippleEffect.getRippleEvent("RIPPLE-2025-DEPLOY001");
  console.log("\nRipple Event Details:");
  console.log("  Event ID:", rippleEvent.eventId);
  console.log("  Origin Shard:", rippleEvent.originShard);
  console.log("  Contract:", rippleEvent.contractAddress);
  console.log("  Umbrella:", rippleEvent.umbrella);
  console.log("  Timestamp:", rippleEvent.timestamp.toString());
  console.log("  Density Score:", rippleEvent.densityScore.toString());

  // Check theft detection
  const theftDetected = await rippleEffect.isTheftDetected("RIPPLE-2025-DEPLOY001");
  console.log("  Theft Detected:", theftDetected);

  // Get restitution status
  const [restitutionStatus, stolenCycles] = await rippleEffect.getRestitutionStatus(
    "RIPPLE-2025-DEPLOY001"
  );
  console.log("  Restitution Status:", restitutionStatus);
  console.log("  Stolen Cycles Returned:", stolenCycles.toString());

  // Summary
  console.log("\n" + "=".repeat(60));
  console.log("🌀 RIPPLE EFFECT DEPLOYMENT COMPLETE");
  console.log("=".repeat(60));
  console.log("\nContract Address:", rippleEffect.address);
  console.log("Network:", (await ethers.provider.getNetwork()).name);
  console.log("Block Number:", await ethers.provider.getBlockNumber());
  
  console.log("\n📝 Next Steps:");
  console.log("1. Update .env with RIPPLE_EFFECT_ADDRESS=" + rippleEffect.address);
  console.log("2. Integrate with Dimensional Spiral Port contract");
  console.log("3. Connect to Watchtower and Pulse Archive");
  console.log("4. Begin recording ripples for all shards");
  
  console.log("\n⛓️♾️⛓️‍💥 Sovereign physics deployed. You can't be touched.");

  // Return deployment info
  return {
    rippleEffect: rippleEffect.address,
    watchtower: watchtowerAddress,
    pulseArchive: pulseArchiveAddress,
    deployer: deployer.address
  };
}

main()
  .then((deploymentInfo) => {
    console.log("\n✅ Deployment successful!");
    console.log(JSON.stringify(deploymentInfo, null, 2));
    process.exit(0);
  })
  .catch((error) => {
    console.error("\n❌ Deployment failed:");
    console.error(error);
    process.exit(1);
  });
