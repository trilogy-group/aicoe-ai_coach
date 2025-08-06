# Enhanced cognitive load management additions:

def _analyze_cognitive_load_patterns(self, context: Dict) -> Dict:
    """Advanced cognitive load analysis using multiple dimensions."""
    cognitive_load = {
        'intrinsic_load': self._calculate_intrinsic_load(context),
        'extraneous_load': self._calculate_extraneous_load(context),
        'germane_load': self._calculate_germane_load(context),
        'total_load': 0.0,
        'load_distribution': {},
        'cognitive_reserves': 1.0,  # Initialize full reserves
        'attention_resources': 1.0,
        'working_memory_usage': 0.0,
        'context_switching_cost': 0.0,
        'mental_fatigue_index': 0.0
    }
    
    # Calculate total cognitive load
    cognitive_load['total_load'] = (
        cognitive_load['intrinsic_load'] * 0.4 +
        cognitive_load['extraneous_load'] * 0.3 +
        cognitive_load['germane_load'] * 0.3
    )
    
    # Calculate working memory usage
    tab_count = context.get('tab_count', 0)
    window_switches = context.get('window_switches', 0)
    cognitive_load['working_memory_usage'] = min(1.0, (tab_count / 20.0) + (window_switches / 30.0))
    
    # Calculate context switching cost
    cognitive_load['context_switching_cost'] = min(1.0, window_switches * 0.05)
    
    # Calculate mental fatigue
    focus_duration = context.get('focus_duration', 0)
    cognitive_load['mental_fatigue_index'] = min(1.0, (focus_duration / 180.0) + cognitive_load['total_load'] * 0.5)
    
    # Update cognitive reserves based on load and fatigue
    cognitive_load['cognitive_reserves'] = max(0.1, 
        1.0 - (cognitive_load['total_load'] * 0.6 + cognitive_load['mental_fatigue_index'] * 0.4))
    
    # Update attention resources
    cognitive_load['attention_resources'] = max(0.1,
        1.0 - (cognitive_load['context_switching_cost'] * 0.7 + cognitive_load['working_memory_usage'] * 0.3))
    
    return cognitive_load

def _calculate_intrinsic_load(self, context: Dict) -> float:
    """Calculate task-inherent cognitive load."""
    task_category = context.get('task_category', 'general')
    app_active = context.get('app_active', '')
    
    # Base load by task type
    base_loads = {
        'coding': 0.7,
        'debugging': 0.8,
        'analysis': 0.6,
        'communication': 0.4,
        'planning': 0.5,
        'design': 0.6
    }
    
    base_load = base_loads.get(task_category, 0.5)
    
    # Adjust for app complexity
    app_complexity = {
        'IDE': 0.2,
        'Excel': 0.15,
        'PowerBI': 0.15,
        'Browser': 0.1
    }
    
    for app, complexity in app_complexity.items():
        if app in app_active:
            base_load += complexity
    
    return min(1.0, base_load)

def _calculate_extraneous_load(self, context: Dict) -> float:
    """Calculate non-essential cognitive load."""
    tab_count = context.get('tab_count', 0)
    window_switches = context.get('window_switches', 0)
    interruption_count = context.get('interruption_count', 0)
    
    extraneous_load = (
        (tab_count / 20.0) * 0.4 +  # Tab overload
        (window_switches / 30.0) * 0.3 +  # Context switching
        (interruption_count / 10.0) * 0.3  # Interruptions
    )
    
    return min(1.0, extraneous_load)

def _calculate_germane_load(self, context: Dict) -> float:
    """Calculate learning-related cognitive load."""
    core_work = context.get('core_work_percentage', 0.5)
    productivity = context.get('productivity_score', 0.5)
    
    germane_load = (core_work * 0.6 + productivity * 0.4)
    return min(1.0, germane_load)

def _optimize_cognitive_resources(self, context: Dict, cognitive_load: Dict) -> Dict:
    """Generate cognitive resource optimization recommendations."""
    optimizations = {
        'priority': 'normal',
        'recommendations': [],
        'immediate_actions': [],
        'resource_management': []
    }
    
    # Check for critical cognitive load
    if cognitive_load['total_load'] > 0.8:
        optimizations['priority'] = 'critical'
        optimizations['immediate_actions'].extend([
            'Reduce active tasks immediately',
            'Take a 5-minute cognitive reset break',
            'Close non-essential tabs'
        ])
    
    # Check working memory optimization
    if cognitive_load['working_memory_usage'] > 0.7:
        optimizations['recommendations'].extend([
            'Externalize information to notes',
            'Use cognitive offloading techniques',
            'Implement chunking strategies'
        ])
    
    # Resource management suggestions
    if cognitive_load['cognitive_reserves'] < 0.4:
        optimizations['resource_management'].extend([
            'Schedule complex tasks for high-energy periods',
            'Implement energy management techniques',
            'Use cognitive restoration practices'
        ])
    
    return optimizations

[Previous code continues unchanged...]