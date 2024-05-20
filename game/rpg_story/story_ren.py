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

    def get_story(self, stage_name):
        return self.stage_map[stage_name][0]
