import pandas as pd


BROKER = "Exness"
PLATFORM = "MT5"
MODE = "DEMO"


def analyze_market(data):
    """
    Simple demo market analysis.
    This version does NOT place real trades.
    """

    if len(data) < 30:
        return "HOLD"

    data["SMA_10"] = data["close"].rolling(10).mean()
    data["SMA_30"] = data["close"].rolling(30).mean()

    fast = data["SMA_10"].iloc[-1]
    slow = data["SMA_30"].iloc[-1]

    if fast > slow:
        return "BUY"

    elif fast < slow:
        return "SELL"

    return "HOLD"


def main():
    print("=" * 45)
    print("EXNESS TRADING BOT")
    print("=" * 45)
    print(f"Broker   : {BROKER}")
    print(f"Platform : {PLATFORM}")
    print(f"Mode     : {MODE}")
    print("=" * 45)

    try:
        data = pd.read_csv("data.csv")
    except FileNotFoundError:
        print("data.csv not found.")
        return

    if "close" not in data.columns:
        print("ERROR: data.csv must contain a 'close' column.")
        return

    decision = analyze_market(data)

    print(f"Market Decision: {decision}")

    if decision == "BUY":
        print("Demo action: BUY")

    elif decision == "SELL":
        print("Demo action: SELL")

    else:
        print("Demo action: HOLD")

    print()
    print("No real-money trade was executed.")


if __name__ == "__main__":
    main()
