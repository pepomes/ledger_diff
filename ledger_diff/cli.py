"""Console script for ledger_diff."""
import sys
import click
import pandas as pd
import uuid

@click.command()
@click.argument('new file')
@click.argument('old file')
def main(new_file, old_file):
    """Console script for ledger_diff."""
    index_cols = ["party", "venue", "account_name", "account_type", "asset"]
    df_new = pd.read_csv(new_file).set_index(index_cols)
    df_old = pd.read_csv(old_file).set_index(index_cols)
    df_diff = df_new.join(df_old, rsuffix="_old").assign(diff=lambda x: x.amount - x.amount_old)
    df_diff.to_csv(f"diff_{uuid.uuid4().int}.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
