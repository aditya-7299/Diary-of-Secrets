init python:
    class QuestManager:
        def __init__(self):
            # Format: { 'quest_id': {'title': str, 'description': str, 'status': str, 'protagonist': str} }
            self.quests = {}
            self.active_quest_id = None
            
        def register(self, quest_id, title, description, protagonist):
            self.quests[quest_id] = {
                "title": title,
                "description": description,
                "status": "hidden",
                "protagonist": protagonist
            }
            
        def start(self, quest_id):
            if quest_id in self.quests:
                self.quests[quest_id]["status"] = "active"
                self.active_quest_id = quest_id
                
        def complete(self, quest_id):
            if quest_id in self.quests:
                self.quests[quest_id]["status"] = "completed"
                if self.active_quest_id == quest_id:
                    self.active_quest_id = None

        def get_active_quest(self):
            if self.active_quest_id and self.active_quest_id in self.quests:
                # Ensure the quest belongs to the currently active protagonist
                q = self.quests[self.active_quest_id]
                if q['protagonist'] == store.current_protagonist:
                    return q
            return None

default q_manager = QuestManager()