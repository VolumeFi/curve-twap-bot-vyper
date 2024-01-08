#!/usr/bin/python3

from conftest import function_signature
from eth_abi import encode
import ape


def test_deposit(TWAPBotContract, VETH, USDC, Alice):
    pool = "0x7F86Bf177Dd4F3494b841a37e810A34dD56c829B"
    route = [
        VETH, pool, USDC,
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000"]
    swap_params = [
        [2, 0, 1, 3, 3],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    amount = 10 ** 18
    pools = [
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000"]
    number_trades = 2
    interval = 60
    starting_time = int(ape.utils.get_current_timestamp_ms() / 1000 + 60)
    fee = 15 * 10 ** 15
    TWAPBotContract.deposit(
        [[route, swap_params, amount, pools]], number_trades, interval,
        starting_time, sender=Alice, value=amount + fee)


def test_cancel(TWAPBotContract, VETH, USDC, Alice, Bob):
    pool = "0x7F86Bf177Dd4F3494b841a37e810A34dD56c829B"
    route = [
        VETH, pool, USDC,
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000"]
    swap_params = [
        [2, 0, 1, 3, 3],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    amount = 10 ** 18
    pools = [
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000"]
    number_trades = 2
    interval = 60
    starting_time = int(ape.utils.get_current_timestamp_ms() / 1000 + 60)
    fee = 15 * 10 ** 15
    receipt = TWAPBotContract.deposit(
        [[route, swap_params, amount, pools]], number_trades, interval,
        starting_time, sender=Alice, value=amount + fee)
    logs = TWAPBotContract.Deposited.from_receipt(receipt)
    deposit_id = logs[0]
    with ape.reverts():
        TWAPBotContract.cancel(deposit_id, 0, sender=Bob)
    TWAPBotContract.cancel(deposit_id, 0, sender=Alice)


def test_withdraw(TWAPBotContract, VETH, USDC, Alice, Compass):
    pool = "0x7F86Bf177Dd4F3494b841a37e810A34dD56c829B"
    route = [
        VETH, pool, USDC,
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000"]
    swap_params = [
        [2, 0, 1, 3, 3],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    amount = 10 ** 18
    pools = [
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000",
        "0x0000000000000000000000000000000000000000"]
    profit_taking = 50
    stop_loss = 50
    expire = 2 ** 32
    fee = 10 ** 16
    TWAPBotContract.deposit(
        route, swap_params, amount, pools, profit_taking, stop_loss, expire,
        sender=Alice, value=amount + fee)
    func_sig = function_signature(
        "multiple_swap(uint256[],uint256[],uint256[])")
    enc_abi = encode(["uint256[]", "uint256[]", "uint256[]"], [[0], [0], [2]])
    add_payload = encode(["bytes32"], [b'123456'])
    payload = func_sig + enc_abi + add_payload
    with ape.reverts():
        TWAPBotContract.multiple_swap([0], [0], [2], sender=Compass)
    TWAPBotContract(sender=Compass, data=payload)
