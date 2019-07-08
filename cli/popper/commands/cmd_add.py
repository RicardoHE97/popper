import click

from popper.cli import pass_context, log
from popper.gha import WorkflowRunner
from popper import scm as scm


@click.command('add', short_help='Import workflow from remote repo.')
@click.argument('path', required=True)
@pass_context
def cli(ctx, path):
    """Imports a workflow from a remote project to the current directory,
    placed on the given path.
    """
    try:
        WorkflowRunner.import_from_repo(path, scm.get_git_root_folder())
    except Exception as e:
        log.fail('Failed to import from {}:\n{}'.format(path, e))
