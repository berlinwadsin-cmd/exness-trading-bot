import MetaTrader5 as mt5

print("EXNESS MT5 CONNECTION TEST")
print("-" * 40)

if not mt5.initialize():
    print("MT5 connection FAILED")
    print("Error:", mt5.last_error())
    quit()

print("MT5 connection: SUCCESS")

account = mt5.account_info()

if account is None:
    print("Account information could not be read.")
else:
    print("Server:", account.server)
    print("Currency:", account.currency)
    print("Balance:", account.balance)
    print("Equity:", account.equity)

print("-" * 40)
print("TEST COMPLETE")
print("NO TRADE WAS OPENED.")

mt5.shutdown()
