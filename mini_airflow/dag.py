class DAG:
    _context_stack = []

    def __init__(self, dag_id):
        self.dag_id = dag_id
        self.task_dict = {}
    
    def add_task(self, task):
        task_id = task.node_id
        if task_id in self.task_dict:
            raise ValueError(f"Task {task_id} already exists in DAG {self.dag_id}")
        self.task_dict[task_id] = task
        task.dag = self
    
    def get_task(self, task_id):
        return self.task_dict.get(task_id)
    
    def __repr__(self):
        """
        내부구조 print()로 보여줌.
        """
        return f"<DAG id={self.dag_id} tasks={list(self.task_dict.keys())}>"
    
    def __enter__(self):
        """
        with문을 사용할 수 있도록함
        """
        DAG._context_stack.append(self)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Docstring for __exit__
        
        :param exc_type: 발생한 에러의 “종류” (예: ValueError, TypeError)
        :param exc_val: 에러 객체(메시지, 값 등 포함)
        :param exc_tb: traceback 객체(에러가 어디서 났는지 경로)
        """
        DAG._context_stack.pop()