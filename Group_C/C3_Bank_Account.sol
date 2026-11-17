// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Simple personal bank account: deposits, withdrawals and balance.
contract CustomerBankAccount {
    address public immutable owner;
    event Deposited(address indexed from, uint256 amount);
    event Withdrawn(address indexed to, uint256 amount);

    constructor() { owner = msg.sender; }

    modifier onlyOwner() { require(msg.sender == owner, "Owner only"); _; }

    function deposit() external payable {
        require(msg.value > 0, "Deposit must be positive");
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be positive");
        require(amount <= address(this).balance, "Insufficient balance");
        (bool sent, ) = payable(owner).call{value: amount}("");
        require(sent, "Transfer failed");
        emit Withdrawn(owner, amount);
    }

    function displayBalance() external view returns (uint256) {
        return address(this).balance; // Balance in wei (1 ETH = 10^18 wei).
    }
}
