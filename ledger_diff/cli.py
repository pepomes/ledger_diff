"""Console script for ledger_diff."""
import sys
import click
import pandas as pd
import datetime as dt

@click.command()
@click.argument('new_file')
@click.argument('old_file')
def main(new_file, old_file):
    """Console script for ledger_diff."""
    index_cols = ["party", "venue", "account_name", "account_type", "asset"]
    df_new = pd.read_csv(new_file).set_index(index_cols)
    df_old = pd.read_csv(old_file).set_index(index_cols)
    df_diff = df_new.join(df_old, how="outer", rsuffix="_old").fillna(0).assign(diff=lambda x: x.amount - x.amount_old)
    df_diff.to_csv(f"diff_{dt.datetime.now().isoformat()}.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
