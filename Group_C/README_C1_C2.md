# Group C: MetaMask practicals C1 and C2

## C1 — Install/configure MetaMask; examine Ether transaction costs
1. Open the official https://metamask.io website and install the browser extension from its official store listing.
2. Create a wallet and set a strong password. Back up the secret recovery phrase **offline**; never share or paste it into websites or examination submissions.
3. In MetaMask's network selector, enable test networks and select **Sepolia**. Get Sepolia test ETH from a reputable faucet (availability varies).
4. Send a small test transaction to a second wallet address you control; confirm the network and recipient before sending.
5. Open the transaction in MetaMask Activity, then view its details in a Sepolia block explorer.
6. Record gas used, effective gas price and transaction fee. Calculate `transaction fee (ETH) = gas used × effective gas price (gwei) / 1,000,000,000`. Example: 21,000 gas × 2 gwei = 0.000042 ETH.
7. Compare fees for simple transfers and smart-contract interactions; note that gas estimates and fees vary.

## C2 — Create/configure a personal MetaMask wallet; transact
1. Install MetaMask from the official source, choose **Create a new wallet**, and securely back up the recovery phrase offline.
2. Verify the wallet address using the account selector; choose the **Sepolia test network**.
3. Obtain free Sepolia test ETH from a faucet. Never use real funds for this lab.
4. Copy the destination address of another wallet you control; in MetaMask select **Send**, paste the address and enter a small test ETH amount.
5. Review recipient, network, estimated gas fee and amount; confirm the transaction.
6. Inspect the pending/completed status and transaction hash in Activity and on a Sepolia explorer.
7. Capture the wallet/network/transaction hash and gas fee for your lab record. **Do not include private keys or recovery phrases in screenshots.**

**Safety:** Testnet ETH has no monetary value. Only interact with trusted links and contracts. Never enter a seed phrase into a faucet.
