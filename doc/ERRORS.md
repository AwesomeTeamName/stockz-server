# Errors
| Class                       | Description                                         |
|:---------------------------:|-----------------------------------------------------|
| `errors.StockzError`        | A base exception class that should not be raised    |
| `errors.ActionError`        | Raised when an error occurs inside an action        |
| `errors.InvalidActionError` | Raised when an invalid action is provided           |
| `errors.CreditsError`       | Raised when the user does not have enough credits   |
| `errors.StockError`         | Raised when the user does not have enough stocks    |
| `errors.InvalidStockError`  | Raised when an invalid stock is provided            |

# Special Errors
### `errors.ActionError(action, *args)`
### `errors.InvalidActionError(action = None, *args)`
