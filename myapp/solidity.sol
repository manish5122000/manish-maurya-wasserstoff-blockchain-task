// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;


contract CrowdFunding{
    mapping (address=>uint) public contributors;
    address public manager;
    uint public minimimContribution;
    uint public deadline;
    uint public target;
    uint public raisedAmount;
    uint public noOfContributors;

    struct Request{
        string description;
        address payable recipients;
        uint value;
        bool completed;
        uint noOfVoters;
        mapping(address => bool) voters;
    }
    mapping (uint=> Request) public  requests;
    uint public numRequest;

    constructor(uint _target, uint _deadline){
        target = _target;
        deadline = block.timestamp + _deadline;
        minimimContribution=100 wei;
        manager = msg.sender;

    }

    function sendEth() public payable {
        require(block.timestamp < deadline, "Deadline has passed");
        require(msg.value >= minimimContribution, "Minimum Contribution is not met");

        if(contributors[msg.sender] == 0){
            noOfContributors++;
        }
        contributors[msg.sender] += msg.value;
        raisedAmount +=msg.value;

    }
    function getContractBalance() public  view returns(uint){
        return address(this).balance;
    }

    function refund() public{
        require(block.timestamp> deadline && raisedAmount< target, "You are not eligible for refund");
        require(contributors[msg.sender]>0);
        address payable user=payable(msg.sender);
        user.transfer(contributors[msg.sender]);
        contributors[msg.sender] == 0;
    
    }

    modifier onlyManager() {
        require(msg.sender == manager, "Only manager can call this function");
        _;
    }
    function createRequest(string memory _description, address payable _recipients, uint _value) public onlyManager{
        Request storage newRequest = requests[numRequest];
        numRequest++;
        newRequest.description = _description;
        newRequest.recipients = _recipients;
        newRequest.value = _value;
        newRequest.completed = false;
        newRequest.noOfVoters = 0;
    }

    function voteRequest(uint _requestNo) public{
        require(contributors[msg.sender]>0, "You must be a contributor");
        Request storage thisRequest = requests[_requestNo];
        require(thisRequest.voters[msg.sender] == false, "You have already vote");
        thisRequest.voters[msg.sender] =true;
        thisRequest.noOfVoters++;
    }

    function makePayment(uint _requestNo) public onlyManager{
        require(raisedAmount>=target);
        Request storage thisRequest=requests[_requestNo];
        require (thisRequest.completed==false, "This reques has been completed");
        require(thisRequest.noOfVoters> noOfContributors/2, "Majority does not support");
        thisRequest.recipients.transfer(thisRequest.value);
        thisRequest.completed = true;
    }
}