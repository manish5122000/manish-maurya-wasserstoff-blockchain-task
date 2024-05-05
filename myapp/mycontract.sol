// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LockingContract {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    event TokensLocked(address indexed sender, address indexed targetAddress, address indexed token, uint256 amount, uint256 releaseTime);
    event TokensReleased(address indexed sender, address indexed token, uint256 amount);

    mapping(address => mapping(address => uint256)) public lockedAmounts;
    mapping(address => mapping(address => uint256)) public releaseTimes;

    function lockTokens(address token, uint256 amount, address targetAddress) external {
        uint256 releaseTime = block.timestamp.add(7 days); // 7 days from now
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        lockedAmounts[targetAddress][token] = lockedAmounts[targetAddress][token].add(amount);
        releaseTimes[targetAddress][token] = releaseTime;

        emit TokensLocked(msg.sender, targetAddress, token, amount, releaseTime);
    }

    function releaseTokens(address token, uint256 amount) external {
        uint256 lockedAmount = lockedAmounts[msg.sender][token];
        require(lockedAmount >= amount, "Insufficient locked amount");
        require(block.timestamp >= releaseTimes[msg.sender][token], "Release time not reached");

        IERC20(token).safeTransfer(msg.sender, amount);
        lockedAmounts[msg.sender][token] = lockedAmount.sub(amount);

        emit TokensReleased(msg.sender, token, amount);
    }
}
