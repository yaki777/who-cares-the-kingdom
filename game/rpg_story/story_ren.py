from rpg_system.renpy_constant import world_controller

"""renpy
init -100 python:
"""


class Story:
    def __init__(self):
        self.name = "TEST_STORY"
        self.current_stage = ""
        self.init_stage = ""

    def stages(self):
        return list(filter(lambda x: 'stage_' in x, dir(self)))


class StoryController:
    def __init__(self):
        self.stage_map = {}
        self.current_stage_list = []
        self.schedule = []

    def start(self):
        for clazz in Story.__subclasses__():
            story = clazz()
            if len(story.init_stage) > 0:
                story.current_stage = story.init_stage
                story.__getattribute__(story.current_stage)()
            for stage in story.stages():
                self.stage_map[story.name + "_" + stage] = (story, stage)

    def start_stage(self, stage_name, *args):
        story, stage = self.stage_map[stage_name]
        story.current_stage = stage
        story.__getattribute__(stage)(*args)

    def schedule_start_stage(self, date, stage_name, *args):
        self.schedule.append((date, stage_name, args))
        sorted(self.schedule, key=lambda x: x[0])

    def get_story(self, stage_name):
        return self.stage_map[stage_name][0]

    def do_schedule(self):
        for (date, stage_name, args) in self.schedule:
            if world_controller.date >= date:
                self.start_stage(stage_name, *args)
        self.schedule = list(filter(lambda x: x[0] > world_controller.date, self.schedule))
