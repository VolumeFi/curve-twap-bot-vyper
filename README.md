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

| Key           | Type          | Description                         |
| ------------- | ------------- | ----------------------------------- |
| route         | address[11]   | Swapping route on Curve swap router |
| swap_params   | uint256[5][5] | Swap params on Curve                |
| amount        | uint256       | Deposit token amount                |
| pools         | address[5]    | Swap pools address on Curve         |
| number_trades | uint256       | Number of TWAP trades               |
| interval      | uint256       | TWAP interval                       |
| starting_time | uint256       | Starting timestamp of TWAP          |

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
| depositor        | address       | Depositor address          |
| route            | address[11]   | Swap route on Curve swap   |
| swap_params      | uint256[5][5] | Swap params on Curve swap  |
| pools            | address[5]    | Swap pools on Curve swap   |
| input_amount     | uint256       | Input amount to trade      |
| number_trades    | uint256       | Initial trading count      |
| interval         | uint256       | Interval                   |
| remaining_counts | uint256       | Remaining trading count    |
| starting_time    | uint256       | Starting timestamp of TWAP |

