# Parses Clicker data attributes
attr_match = {
    'ans' : 'final_response',   
    'fanst' : 'final_answer_time',
    'att' : 'num_attemps',
    'tm' : 'time',
    'scr' : 'score',
    'lto' : 'loaned_clicker_to',
    'fans' : 'first_response',
    'tscr' : 'total_score',
    'id' : 'clicker_id',
    'quuid' : 'question_unique_id',
    'anypt' : 'any_choice_response',
    'isap' : 'is_anonymous_polling',
    'sig' : 'significant_characters',
    'strt' : 'start_time',
    'anspt' : 'correct_answer_points',
    'qn' : 'question_name',
    'isspp' : 'is_self_paced',
    'idx': 'question_index',
    'qType' : 'question_type', 
    'cans' : 'correct_answer', 
    'stp': 'stop_time', 
    'isDel' : 'is_deleted'
}
def parse_attr(attr_list):
    header_row = {}
    for i in range(0, len(attr_list)):
        attr = attr_list[i]
        if attr in attr_match:
            header_row[attr] = attr_match[attr]
        else: 
            header_row[attr] = attr
    return header_row