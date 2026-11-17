// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Student information with struct, array, receive and fallback.
contract StudentInformation {
    address public immutable owner;
    struct Student { uint256 rollNo; string name; uint256 marks; }
    Student[] private students;
    mapping(uint256 => bool) public rollExists;
    event StudentAdded(uint256 indexed rollNo, string name, uint256 marks);
    event EtherReceived(address indexed sender, uint256 amount);
    event FallbackCalled(address indexed sender, uint256 amount, bytes data);

    constructor() { owner = msg.sender; }
    modifier onlyOwner() { require(msg.sender == owner, "Owner only"); _; }

    function addStudent(uint256 rollNo, string calldata name, uint256 marks) external onlyOwner {
        require(!rollExists[rollNo], "Duplicate roll number");
        require(bytes(name).length > 0, "Name required");
        require(marks <= 100, "Marks must be 0..100");
        rollExists[rollNo] = true;
        students.push(Student(rollNo, name, marks));
        emit StudentAdded(rollNo, name, marks);
    }

    function getStudent(uint256 index) external view returns (uint256, string memory, uint256) {
        require(index < students.length, "Invalid index");
        Student storage s = students[index];
        return (s.rollNo, s.name, s.marks);
    }
    function studentCount() external view returns (uint256) { return students.length; }
    receive() external payable { emit EtherReceived(msg.sender, msg.value); }
    fallback() external payable { emit FallbackCalled(msg.sender, msg.value, msg.data); }
}
