#!/usr/bin/python3

import pytest
from eth_abi import encode
from web3 import Web3


@pytest.fixture(scope="session")
def Deployer(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def Alice(accounts):
    return accounts[1]


@pytest.fixture(scope="session")
def Bob(accounts):
    return accounts[2]


@pytest.fixture(scope="session")
def RefundWallet(accounts):
    return accounts[3]


@pytest.fixture(scope="session")
def ServiceFeeCollector(accounts):
    return accounts[4]


@pytest.fixture(scope="session")
def Compass(accounts):
    return accounts[5]


@pytest.fixture(scope="session")
def CurveRouter(project):
    return project.curve_router.at(
        "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D")


@pytest.fixture(scope="session")
def VETH():
    return "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"


@pytest.fixture(scope="session")
def WETH(project):
    return project.weth.at("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")


@pytest.fixture(scope="session")
def USDC(project):
    return project.usdc.at("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")


@pytest.fixture(scope="session")
def TWAPBotContract(
        Compass, CurveRouter, RefundWallet, ServiceFeeCollector, Deployer,
        project):
    fee = 15 * 10 ** 15  # 0.015ETH
    service_fee = 2 * 10 ** 15  # 0.2%
    contract = Deployer.deploy(
        project.curve_limit_order_bot, Compass, CurveRouter, RefundWallet,
        fee, ServiceFeeCollector, service_fee)
    func_sig = function_signature("set_paloma()")
    add_payload = encode(["bytes32"], [b'123456'])
    payload = func_sig + add_payload
    contract(sender=Compass, data=payload)
    return contract


def function_signature(str):
    return Web3.keccak(text=str)[:4]
