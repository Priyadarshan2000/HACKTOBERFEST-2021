// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts v4.3.2 (token/ERC20/IERC20.sol)
pragma solidity ^0.5.3;

/**
 * @dev Interface of the ERC20 standard as defined in the EIP.
 */
interface IERC20 {
    /**
     * @dev Returns the amount of tokens in existence.
     */
    function totalSupply() external view returns (uint256);

    /**
     * @dev Returns the amount of tokens owned by `account`.
     */
    function balanceOf(address account) external view returns (uint256);

    /**
     * @dev Moves `amount` tokens from the caller's account to `recipient`.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transfer(address recipient, uint256 amount) external returns (bool);

    /**
     * @dev Returns the remaining number of tokens that `spender` will be
     * allowed to spend on behalf of `owner` through {transferFrom}. This is
     * zero by default.
     *
     * This value changes when {approve} or {transferFrom} are called.
     */
    function allowance(address owner, address spender) external view returns (uint256);

    /**
     * @dev Sets `amount` as the allowance of `spender` over the caller's tokens.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * IMPORTANT: Beware that changing an allowance with this method brings the risk
     * that someone may use both the old and the new allowance by unfortunate
     * transaction ordering. One possible solution to mitigate this race
     * condition is to first reduce the spender's allowance to 0 and set the
     * desired value afterwards:
     * https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
     *
     * Emits an {Approval} event.
     */
    function approve(address spender, uint256 amount) external returns (bool);

    /**
     * @dev Moves `amount` tokens from `sender` to `recipient` using the
     * allowance mechanism. `amount` is then deducted from the caller's
     * allowance.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    /**
     * @dev Emitted when `value` tokens are moved from one account (`from`) to
     * another (`to`).
     *
     * Note that `value` may be zero.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Emitted when the allowance of a `spender` for an `owner` is set by
     * a call to {approve}. `value` is the new allowance.
     */
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract myERC20 is IERC20{
    mapping(address=>uint) _balances;
    mapping(address=>mapping(address=>uint)) _allowed;
    string public name = "NickDoge";
    string public symbol = "NID";
    uint public decimals = 0;
    
    //inital supply
    uint private _totalsupply;
    //creator's address
    address public _creator;
    
    constructor() public{
        _creator = msg.sender;
        _totalsupply = 50000;
        _balances[_creator] = _totalsupply;
    }
    
    function totalSupply() external view returns (uint256){
        return _totalsupply;
    }
    
    function balanceOf(address account) external view returns (uint256){
        return _balances[account];
    }
    
    function transfer(address recipient, uint256 amount) public returns (bool){
        require(amount>0 && _balances[msg.sender]>= amount);
        _balances[recipient]+=amount;
        _balances[msg.sender]-=amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }
    
    function approve(address spender, uint256 amount) external returns (bool){
        require(amount>0 && _balances[msg.sender]>= amount);
        _allowed[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
    }
    
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool){
        require(amount>0 && _balances[sender]>= amount && _allowed[sender][recipient]>=amount);
        _balances[recipient]+=amount;
        _balances[sender]-=amount;
        _allowed[sender][recipient] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }
    
    function allowance(address owner, address spender) external view returns (uint256){
        return _allowed[owner][spender];
    }
    
    
}


contract ICOblock is myERC20{
    //admin
    address public admin;
    //where eth is recieved
    address payable public recipientAccount;
    //price of each token, 0.01 eth
    uint public tokPrice = 1000000000000000;
    //hardcap 500eth
    uint public icoTarget = 500000000000000000000;
    // track funded amount
    uint public receivedFund;
    uint public maxinv = 10000000000000000000;
    uint public mininv = 1000000000000000;
    
    uint public startTrading = icoendTime;
    
    enum Status {inactive, active, stopped, completed}
    Status public icoStatus;
    uint public icoStartTime = now; 
    uint public icoendTime = now + 43200; 
    
    modifier onlyOwner{
        if(msg.sender == admin){
            _;
        }
    }
    
    constructor(address payable _recipient)public{
        admin = msg.sender;
       recipientAccount = _recipient;
    }
    
    function setStopStatus() public onlyOwner{
        icoStatus = Status.stopped;
    }
    
    function setActiveStatus() public onlyOwner{
        icoStatus = Status.active;
    }
    
    function getIcoStatus() public view returns(Status){
        if(icoStatus == Status.stopped){
            return Status.stopped;
        }else if(block.timestamp >= icoStartTime &&
        block.timestamp <= icoendTime){
            return Status.active;
        }else if(block.timestamp <= icoendTime){
            return Status.inactive;
        }else{
            return Status.completed;
        }
    }
    
    function invest() payable public returns(bool){
        icoStatus = getIcoStatus();
        require(icoStatus == Status.active, "ICO is not active");
        require(receivedFund+msg.value <= icoTarget, "Target Funding Reached");
        require(msg.value<=maxinv && msg.value>=mininv, "Boundary Conditions not achieved");
        uint tokens = msg.value/tokPrice;
        _balances[msg.sender] += tokens;
        _balances[_creator] -= tokens;
        recipientAccount.transfer(msg.value);
        receivedFund += msg.value;
        return true;
    }
    
    function burn() public onlyOwner returns(bool){
        icoStatus = getIcoStatus();
        require(icoStatus == Status.completed, "ICO is not yet completed");
        _balances[_creator] = 0;
        return true;
    }
    
    function transfer(address recipient, uint256 amount) public returns (bool){
        require(block.timestamp>startTrading, "Trading not allowed");
        super.transfer(recipient, amount);
        return true;
    }
    
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool){
        require(block.timestamp>startTrading, "Trading not allowed");
        super.transferFrom(sender, recipient, amount);
        return true;
    }
    
}