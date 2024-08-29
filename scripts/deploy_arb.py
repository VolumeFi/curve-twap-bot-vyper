from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    max_base_fee = int(networks.active_provider.base_fee * 1.2)
    compass = "0x82Ed642F4067D55cE884e2823951baDfEdC89e73"
    curve_router = "0x2191718CD32d02B8E60BAdFFeA33E4B5DD9A0A0D"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 0
    service_fee_collector = "0xe693603C9441f0e645Af6A5898b76a60dbf757F4"
    service_fee = 2000000000000000
    result = project.curve_twap_bot.deploy(
        compass, curve_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=min(int(0.01e9), max_base_fee), sender=acct)
    print(result)
