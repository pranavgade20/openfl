from pathlib import Path

from tests.github.interactive_api_director import utils


if __name__ == '__main__':
    root_dir = Path(__file__).parent
    director = utils.start_director(root_dir / 'director', 'config.yaml')
    envoy = utils.start_envoy(root_dir / 'envoy', 'envoy_config.yaml')
    from tests.github.interactive_api_director.experiments.tensorflow_mnist import experiment
    experiment.run()