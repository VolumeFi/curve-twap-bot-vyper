# Curve TWAP BOT

## Read-Only functions

### multiple_swap_view

This function was built to be called as view function. So function type in ABI should be fixed to view.

| Key              | Type      | Description                                 |
| ---------------- | --------- | ------------------------------------------- |
| deposit_id       | uint256[] | deposit ids to get expected amounts         |
| remaining_counts | uint256[] | remaining counts of the swapping            |
| **Return**       | address[] | Returns expected amounts from the swappings |

### next_deposit

| Key        | Type    | Description             |
| ---------- | ------- | ----------------------- |
| **Return** | uint256 | Returns next deposit id |

### deposit_list

| Key        | Type    | Description                           |
| ---------- | ------- | ------------------------------------- |
| *arg0*     | uint256 | Deposit Id to get Deposit information |
| **Return** | Deposit | Deposit information                   |


## State-Changing functions

### deposit

Deposit a token with its amount with an expected token address and amount. This is run by users.

| Key           | Type          | Description                                 |
| ------------- | ------------- | ------------------------------------------- |
| route         | address[9]    | Swapping route on Curve swap router         |
| swap_params   | uint256[3][4] | Deposit token amount                        |
| amount        | uint256       | Expected token amount from the initial swap |
| pools         | address[4]    | Permille of profit_taking                   |
| number_trades | uint256       | Permille of stop_loss                       |
| interval      | uint256       | Permille of stop_loss                       |
| starting_time | uint256       | Permille of stop_loss                       |

### cancel

Cancel order. This is run by users.

| Key        | Type    | Description          |
| ---------- | ------- | -------------------- |
| deposit_id | uint256 | Deposit Id to cancel |


### multiple_swap

Swap and send multiple tokens to the depositor. This is run by Compass-EVM only.

| Key              | Type      | Description                             |
| ---------------- | --------- | --------------------------------------- |
| deposit_ids      | uint256[] | Deposit Id array to swap                |
| remaining_counts | uint256[] | Remaining count of TWAP                 |
| amount_out_min   | uint256[] | minimum amount to receive from swapping |

## Admin functions

### update_compass

Update Compass-EVM address.  This is run by Compass-EVM only.

| Key         | Type    | Description             |
| ----------- | ------- | ----------------------- |
| new_compass | address | New compass-evm address |

### update_refund_wallet

Update gas refund wallet address.  This is run by Compass-EVM only.

| Key               | Type    | Description               |
| ----------------- | ------- | ------------------------- |
| new_refund_wallet | address | New refund wallet address |

### update_fee

Update gas fee amount to pay.  This is run by Compass-EVM only.

| Key     | Type    | Description    |
| ------- | ------- | -------------- |
| new_fee | uint256 | New fee amount |

### set_paloma

Set Paloma CW address in bytes32.  This is run by Compass-EVM only and after setting paloma, the bot can start working.

### update_service_fee_collector

Update service fee collector address.  This is run by the original fee collector address. The address receives service fee from swapping.

| Key                       | Type    | Description                       |
| ------------------------- | ------- | --------------------------------- |
| new_service_fee_collector | address | New service fee collector address |

## Struct

### Deposit

| Key              | Type          | Description                |
| ---------------- | ------------- | -------------------------- |
| depositor        | address       | depositor address          |
| route            | address[9]    | Swap route on Curve swap   |
| swap_params      | uint256[3][4] | Swap params on Curve swap  |
| pools            | address[4]    | Swap pools on Curve swap   |
| input_amount     | uint256       | input amount to trade      |
| number_trades    | uint256       | initial trading count      |
| interval         | uint256       | interval                   |
| remaining_counts | uint256       | remaining trading count    |
| starting_time    | uint256       | start timestamp of the bot |

