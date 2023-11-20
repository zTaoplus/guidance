
#GroupbyAgg
group_by_agg_str ="""{{~#if contains(this.command, "GroupbyAgg")}}
            "command_args":{
                "by": "⊕{{~gen "this.by" temperature=0.01 stop='⊗'}}⊗",
                "agg_args": "⊕{{~gen "this.agg_args" temperature=0.01 stop='⊗'}}⊗"
                },
                {{~/if}}"""


            
#GroupbyTransform
group_by_transform_str = """
            {{~#if contains(this.command, "GroupbyTransform")}}
            "command_args":{
                "by": "⊕{{~gen "this.by" temperature=0.01 stop='⊗'}}⊗",
                "transform_args": {
                    "transform_cols": "⊕{{~gen "this.transfrom_cols" temperature=0.01 stop='⊗'}}⊗",
                    "transform_type": "⊕{{~gen "this.function_name" temperature=0.01 stop='⊗'}}⊗"
                    },
                "replace": "⊕{{~gen "this.replace" temperature=0.01 stop='⊗'}}⊗",
                "new_cols": "⊕{{~gen "this.new_cols" temperature=0.01 stop='⊗'}}⊗"
                },        
            {{~/if}}"""



#FeatureTransAgg
feature_trans_agg_str = """
            {{~#if contains(this.command, "FeatureTransAgg")}}
            "command_args":{
                "agg_args": "⊕{{~gen "this.agg_args" temperature=0.01 stop='⊗'}}⊗",
                "new_cols": "⊕{{~gen "this.new_cols" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""



#FeatureTransClip
feature_trans_clip_str = """
            {{~#if contains(this.command, "FeatureTransClip")}}
            "command_args":{
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "lower": "⊕{{~gen "this.lower" temperature=0.01 stop='⊗'}}⊗",
                "upper": "⊕{{~gen "this.upper" temperature=0.01 stop='⊗'}}⊗",
                "replace": "⊕{{~gen "this.replace" temperature=0.01 stop='⊗'}}⊗",
                "new_cols": "⊕{{~gen "this.new_cols" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


#DropDuplicates
dropduplicates_str = """
            {{~#if contains(this.command, "DropDuplicates")}}
            "command_args":{
                "subset": "⊕{{~gen "this.subset" temperature=0.01 stop='⊗'}}⊗",
                "keep": "⊕{{~gen "this.keep" temperature=0.01 stop='⊗'}}⊗",
                "subset_only": "⊕{{~gen "this.subset_only" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""



#Dropna
dropna_str = """
            {{~#if contains(this.command, "Dropna")}}
            "command_args":{
                "axis": "⊕{{~gen "this.subset" temperature=0.01 stop='⊗'}}⊗",
                "how": "⊕{{~gen "this.subset" temperature=0.01 stop='⊗'}}⊗",
                "subset": "⊕{{~gen "this.subset" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# Replace
replace_str = """
            {{~#if contains(this.command, "Replace")}}
            "command_args":{
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "index": "⊕{{~gen "this.index" temperature=0.01 stop='⊗'}}⊗",
                "replace_value": "⊕{{~gen "this.replace_value" temperature=0.01 stop='⊗'}}⊗",
                "bool_args": "⊕{{~gen "this.bool_args" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


#Fillna
fillna_str = """
            {{~#if contains(this.command, "Fillna")}}
            "command_args":{
                "fill_value": "⊕{{~gen "this.fill_value" temperature=1.0 stop='⊗'}}⊗",
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "method": "⊕{{~gen "this.method" temperature=0.01 stop='⊗'}}⊗",
                "axis": "⊕{{~gen "this.axis" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# Rename
rename_str = """
            {{~#if contains(this.command, "Rename")}}
            "command_args": {
                "columns_rename": "⊕{{~gen "this.columns_rename" temperature=0.01 stop='⊗'}}⊗",
                "index_rename": "⊕{{~gen "this.index_rename" temperature=0.01 stop='⊗'}}⊗"
                },          
            {{~/if}}"""

# Sort
sort_str = """
            {{~#if contains(this.command, "SortValues")}}
            "command_args":{
                "by": "⊕{{~gen "this.by" temperature=0.1 stop='⊗'}}⊗",
                "ascending": "⊕{{~gen "this.ascending" temperature=0.01 stop='⊗'}}⊗"
                },  
            {{~/if}}"""
# Filter
# TODO
filter_str = """
           {{~#if contains(this.command, "Filter")}}
            "command_args": {
                "bool_args": "⊕{{~gen "this.bool_args" temperature=0.01 stop='⊗'}}⊗",
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "index": "⊕{{~gen "this.index" temperature=0.01 stop='⊗'}}⊗",
                "axis": "⊕{{~gen "this.axis" temperature=0.01 stop='⊗'}}⊗",
                "slice": "⊕{{~gen "this.slice" temperature=0.01 stop='⊗'}}⊗",
                "type": "⊕{{~gen "this.type" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


# FourOperation
four_operation_str = """
            {{~#if contains(this.command, "FourOperation")}}
            "command_args":{
                "value": "⊕{{~gen "this.value" temperature=0.01 stop='⊗'}}⊗",
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "index": "⊕{{~gen "this.index" temperature=0.01 stop='⊗'}}⊗",
                "operation_type": "⊕{{~gen "this.operation_type" temperature=0.01 stop='⊗'}}⊗",
                "new_cols": "⊕{{~gen "this.new_cols" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


# StaticsColumn
statics_column_str = """
            {{~#if contains(this.command, "StaticsColumn")}}
            "command_args": {
                "aggregate": "⊕{{~gen "this.aggregate" temperature=0.01 stop='⊗'}}⊗",
                "is_index": "⊕{{~gen "this.is_index" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# StaticsRow
statics_row_str = """
            {{~#if contains(this.command, "StaticsRow")}}
            "command_args": {
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "index": "⊕{{~gen "this.index" temperature=0.01 stop='⊗"'}}⊗",
                "slice": "⊕{{~gen "this.slice" temperature=0.01 stop='⊗'}}⊗",
                "statistic_type": "⊕{{~gen "this.statistic_type" temperature=0.01 stop='⊗'}}⊗"
                },      
            {{~/if}}"""

# Quantile
quantile_str = """
            {{~#if contains(this.command, "Quantile")}}
            "command_args": {
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "index": "⊕{{~gen "this.index" temperature=0.01 stop='⊗'}}⊗",
                "slice": "⊕{{~gen "this.slice" temperature=0.01 stop='⊗'}}⊗",
                "quantile": "⊕{{~gen "this.quantile" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# Shape
shape_str =  """ 
            {{~#if contains(this.command, "Shape")}}
            "command_args": {
                "type": "⊕{{~gen "this.type" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


#Join
#TODO
join_str = """
            {{~#if contains(this.command, "Join")}}
            "command_args": {
                "ons": "⊕{{~gen "this.ons" temperature=0.01 stop='⊗'}}⊗",
                "how": "⊕{{~gen "this.how" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


# Concat
concat_str = """
            {{~#if contains(this.command, "Concat")}}
            "command_args":{
                "axis": "⊕{{~gen "this.axis" temperature=0.01 stop='⊗'}}⊗",
                "join": "⊕{{~gen "this.join" temperature=0.01 stop='⊗'}}⊗",
                "ignore_index": "⊕{{~gen "this.ignore_index" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# Rolling
rolling_str = """
            {{~#if contains(this.command, "Rolling")}}
            "command_args":{
                "columns":"⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "agg": "⊕{{~gen "this.agg" temperature=0.01 stop='⊗'}}⊗",
                "windows": "⊕{{~gen "this.windows" temperature=0.01 stop='⊗'}}⊗",
                "on": "⊕{{~gen "this.on" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# Resample
resample_str = """
            {{~#if contains(this.command, "Resample")}}
            "command_args":{
                "time_columns": "⊕{{~gen "this.time_columns" temperature=0.01 stop='⊗'}}⊗",
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "how": "⊕{{~gen "this.how" temperature=0.01 stop='⊗'}}⊗",
                "freq": "⊕{{~gen "this.freq" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""

# TimeInterval_str
timeinterval_str = """
            {{~#if contains(this.command, "TimeInterval")}}
            "command_args":{
                "columns": "⊕{{~gen "this.columns" temperature=0.01 stop='⊗'}}⊗",
                "period": "⊕{{~gen "this.period" temperature=0.01 stop='⊗'}}⊗",
                "period_number": "⊕{{~gen "this.period_number" temperature=0.01 stop='⊗'}}⊗",
                "get_current_date": "⊕{{~gen "this.get_current_date" temperature=0.01 stop='⊗'}}⊗",
                "known_time": "⊕{{~gen "this.known_time" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}"""


# visualize_all
visualize_str = """
        {{~#each plot_type item_name="plot_name"}}
            {{~#if contains(this.command, plot_name)}}
            "command_args": {
                "x": "⊕{{~gen "this.x" temperature=0.01 stop='⊗'}}⊗",
                "y": "⊕{{~gen "this.y" temperature=0.01 stop='⊗'}}⊗",
                "transpose": "⊕{{~gen "this.transpose" temperature=0.01 stop='⊗'}}⊗"
                },
            {{~/if}}
        {{~/each}}"""

