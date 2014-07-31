# Protocol
**Maximum packet size**: 2048 bytes

## Format
All requests are strings following the syntax `action sender args`.

Both `action` and `sender` are required, whereas `args` can be omitted.

Neither `action` nor `sender` can contain spaces, but `args` may contain any number of spaces.

### Examples
	buy 01234567891 3 10
	sell 01234567891 1
	credits 01234567891
	stock 01234567891 GOOG

## Actions

### `help`

#### Description
Retrieve a list of all available actions and their descriptions.

---

### `credits`

#### Description
Retrieve the user's number of credits.

---

### `stock`

#### Description
Retrieve information about a stock.

---

### `stocks`

#### Description
Retrieve a list of the top 10 stocks (current value).

---

### `buy`

#### Description
Buy stocks.

---

### `sell`

#### Description
Sell stocks.
