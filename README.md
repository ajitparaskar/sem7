# Laboratory Practice III (410246) — Unique Practical Programs

The uploaded examination PDF repeats the same practicals across three sets. This archive includes **13 unique coding files** and instructions for **2 wallet tasks**, for **15 unique titles**.

## Group A — standalone Python (standard library only)
- A1: Fibonacci numbers and computational step count.
- A2: Greedy job sequencing with deadlines.
- A3: Greedy fractional knapsack.
- A4: 0/1 knapsack via dynamic programming.
- A5: Binomial coefficients via dynamic programming.
- A6: 8-Queens backtracking with the first queen's position fixed.

Run: `python Group_A/A1_Fibonacci.py` (and similarly A2–A6). Press Enter for sample inputs.

## Group B — Python machine learning
- B1: Uber fare preprocessing, outlier detection, correlation, Linear/Random Forest regression, R2/RMSE.
- B2: Email spam classification with KNN and SVM.
- B3: Bank churn neural network classification, normalization, hyperparameter tuning, accuracy/confusion matrix.
- B4: Diabetes KNN, confusion matrix and classification metrics.
- B5: Customer segmentation with K-Means and elbow plot.

Install requirements: `python -m pip install -r requirements.txt`

Run without a dataset (synthetic demonstration only): `python Group_B/B1_Uber_Fare_Prediction.py`

Run with a real CSV: `python Group_B/B1_Uber_Fare_Prediction.py --csv /path/to/uber.csv`

Similarly, pass `--csv /path/to/spam.csv`, `Churn_Modelling.csv`, `diabetes.csv`, or `sales_data_sample.csv` for B2–B5. Real datasets are **not included in the uploaded PDF** and are not bundled here. Scripts explicitly use synthetic example data when `--csv` is omitted. Synthetic results are demonstrations, not valid research performance claims.

Expected target columns: B1 `fare_amount`; B2 `label`/`text` or `v1`/`v2`; B3 `Exited` or `Churn`; B4 `Outcome`; B5 `CUSTOMERNAME`/`SALES` (or numeric features). B5 writes its plot and cluster CSV to the current working directory.

## Group C — Solidity and wallet setup
- C1: Install/configure MetaMask; examine Ether transaction costs (see `Group_C/README_C1_C2.md`).
- C2: Create/configure wallet and perform transactions (same README).
- C3: Bank account deposit, withdraw and balance contract (`C3_Bank_Account.sol`).
- C4: Student information using structs, arrays and fallback (`C4_Student_Information.sol`).

Open https://remix.ethereum.org, create a file matching the `.sol` filename, paste its source, compile with a Solidity 0.8.x compiler, and deploy using Remix VM for free tests. For an actual Sepolia test-network deployment, connect an authorized wallet via Injected Provider and have test ETH for gas. For C3, deploy then set a nonzero Value (e.g. `1 ether`) before calling `deposit`; reset Value to 0 before calling `withdraw` with amount in wei; use `displayBalance` to inspect funds. Only the deploying wallet can withdraw. For C4, call `addStudent(1,"Asha",90)`, `studentCount()` and `getStudent(0)`; Remix shows gas used in transaction details. A `fallback` function runs for calls with unknown function selectors; `receive` handles empty calldata ETH transfers.

## Notes
These are teaching implementations; no CSV data was supplied. Results depend on the actual dataset and installed library versions. Smart contracts are educational examples, not audited for production use.
