from elasticmon.client import ElasticmonClient
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description='Elasticsearch monitoring client')
    parser.add_argument(
        '--verbose',
        '-v',
        action='count',
        dest='verbosity',
        help=
        'verbose mode (-v for warnings, -vv for informational, -vvv for debug')
    parser.add_argument(
        '--es-hosts',
        '-e',
        dest='es_hosts',
        nargs='+',
        help='elasticsearch host(s) to retrieve information from')

    args = parser.parse_args()

    mon_client = ElasticmonClient(verbosity=args.verbosity, hosts=args.es_hosts)
    chealth = mon_client.cluster_health()
    mon_client.print_cluster_health_flattened(j=chealth)

    nstats = mon_client.node_stats()
    mon_client.print_node_stats_flattened(j=nstats)
