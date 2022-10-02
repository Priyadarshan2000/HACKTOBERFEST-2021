pragma solidity ^0.8.0;

contract voting{
    address public owner;
    address [] public candidateList;
    mapping(address=>uint) votes;
    address public winner;
    uint public winnerVotes;
    
    constructor() public{
        owner = msg.sender;
    }
    
    modifier onwerOnly{
        if(msg.sender == owner){
            _;
        }
    }
    
    enum votingStatus {inactive, running, completed}
    votingStatus public status;
    
    function setStatus() onwerOnly public{
        if(status != votingStatus.completed && status == votingStatus.inactive){
            status = votingStatus.running;
        }
        else{
            status = votingStatus.completed;
        }
    }
    
    function registerCandidates(address _candidate)
    onwerOnly public{
        candidateList.push(_candidate);
    }
    
    function vote(address _candidate) public{
        require(validateCandidate(_candidate), "Not a validate Candidate");
        require(status == votingStatus.running, "Voting is Inactive");
        votes[_candidate] +=1;
    }
    
    function validateCandidate(address _candidate) private view returns(bool){
        for(uint i=0; i<candidateList.length; i++){
            if(candidateList[i] == _candidate){
                return true;
            }
        }
        return false;
    }
    
    function votesCount(address _candidate) public view returns(uint){
        require(validateCandidate(_candidate), "Not a validate Candidate");
        assert(status == votingStatus.running);
        return votes[_candidate];
    }
    
    function result() public{
        require(status == votingStatus.completed, "Election is active,Result can't be declared");
        for(uint i=0; i<candidateList.length; i++){
            if(votes[candidateList[i]] > winnerVotes){
                winnerVotes = votes[candidateList[i]];
                winner = candidateList[i];
            }
        }
    }
}