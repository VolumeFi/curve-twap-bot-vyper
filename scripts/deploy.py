from ape import accounts, project, networks


def main():
    acct = accounts.load("deployer_account")
    max_base_fee = int(networks.active_provider.base_fee * 1.2)
    compass = "0xB01cC20Fe02723d43822819ec57fCbadf31f1537"
    curve_router = "0xF0d4c12A5768D806021F80a262B4d39d26C58b8D"
    refund_wallet = "0x6dc0A87638CD75Cc700cCdB226c7ab6C054bc70b"
    fee = 25000000000000000
    service_fee_collector = "0x7a16fF8270133F063aAb6C9977183D9e72835428"
    service_fee = 2000000000000000
    result = project.curve_twap_bot.deploy(
        compass, curve_router, refund_wallet, fee, service_fee_collector,
        service_fee, max_fee=max_base_fee,
        max_priority_fee=min(int(0.01e9), max_base_fee), sender=acct)
    print(result)
