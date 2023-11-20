from dsl_template_st import *


def trim(str):
    # return str.replace('\n', '').replace("    ", "")
    return str



command_args = "".join(
    [
        group_by_agg_str,
        group_by_transform_str,
        feature_trans_agg_str,
        feature_trans_clip_str,
        dropduplicates_str,
        dropna_str,
        replace_str,
        fillna_str,
        rename_str,
        sort_str,
        filter_str,
        four_operation_str,
        statics_column_str,
        statics_row_str,
        quantile_str,
        shape_str,
        join_str,
        concat_str,
        rolling_str,
        resample_str,
        timeinterval_str,
        visualize_str
    ]
)



def format_output():
    template = """
    [
    {{~#geneach 'dsl' join=', ' stop="]"}}
        {
            "input": "⊕{{~gen "this.input" temperature=0.01 stop='⊗'}}⊗",
            "command": "⊕{{~gen "this.command" temperature=0.01 stop='⊗'}}⊗",
            {command_args}
            "output": "⊕{{~gen "this.output" temperature=0.01 stop='⊗'}}⊗"
        }
    {{~/geneach}}
    ]"""
    template = template.replace('{command_args}', command_args)
    return trim(template)




