from typing import Iterable

from .models import Experiment, Group, Variation
from .types import Idfa
from .utils import apply, weighted_choice
from .view_models import ExperimentViewModel, GroupViewModel


class AnalyticsService:
    def list_experiments(self) -> list[ExperimentViewModel]:
        experiments = Experiment.objects.select_experiments_with_variations()
        return apply(ExperimentViewModel.from_experiment, experiments)

    def list_groups(self, idfa: Idfa) -> list[GroupViewModel]:
        groups = Group.objects.select_groups(idfa)
        return apply(GroupViewModel.from_group, groups)

    def populate_and_list_groups(self, idfa: Idfa) -> list[GroupViewModel]:
        experiments = Experiment.objects.select_experiments_that_groups_do_not_participate_in(idfa)
        self.create_new_groups(idfa, experiments)
        return self.list_groups(idfa)

    def create_new_groups(self, idfa: Idfa, experiments: list[Experiment]) -> None:
        new_groups = self.accumulate_new_groups(idfa, experiments)
        Group.objects.bulk_create(new_groups)

    def accumulate_new_groups(self, idfa: Idfa, experiments: list[Experiment]) -> Iterable[Group]:
        for e in experiments:
            variation = self.choose_random_variation(e)
            yield Group(idfa=idfa, variation=variation)

    def choose_random_variation(self, experiment: Experiment) -> Variation:
        variations = experiment.variations.all()
        probabilities = [v.probability for v in variations]
        return weighted_choice(variations, probabilities)
