# python3.5
# Testing

import click


@click.command()
@click.option(
    '--count',
    'count',
    default=1,
    help='Total lines to output',
    required=True,
)
@click.option(
    '--output',
    'output_file',
    default='jacks_file.txt',
    help="File in which to write output",
    required=True,
)
def main(count, output_file):

    output = open(output_file, "w")

    n = 0
    while n < count:
        output.write("All work and no play makes...\n")
        n = n + 1

    output.close()


if __name__ == '__main__':
    main()
