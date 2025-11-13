#Modules to install
import datetime as dt
from IPython.core.display import display

#Optional in case sound is needed
#from IPython.display import Audio

def og(op_type='exec_time',df_list=None, df_rows=1,message=None,division=None,hours_delta=0,sound=None):
    """Display the chosen type of output guide

    Args:
        op_type(str,optional): name of the output type to display
        df_list(list,optional): list of Dataframes
        df_rows(int or str,optional): number of rows to be displayed from all DataFrame
        message(str, optional): message to display
        division(str, optional): string that will be printed at the end as division
        hours_delta(int, optional): number of hours that will be shifted to system date
        sound(bool,optional): sound to play
    """
    try:
        global og_start
        global og_last
        sound_dir = "C:\\Users\\frodriguezu\\Fernando\\system"

        def ex_at_str():
            ex_date = dt.datetime.now() + dt.timedelta(hours=hours_delta)
            return '   >>> '+str(ex_date)

        def exec_time():
            print(ex_at_str())

        def get_name(df):
            for x in globals():
                if globals()[x] is df:
                    name = x
            return name

        def created_df(df_list,df_rows):
            names_list = []
            for df in df_list:
                name = get_name(df)
                names_list.append(name)
            for (name,df) in zip(names_list,df_list):
                if df_rows == 'all':
                    df_rows = df.shape[0]
                print(name)
                print(str(df.shape)+ex_at_str())
                display(df.head(df_rows))

        if message != None: print(message)
        if op_type == 'exec_time':
            og_last = dt.datetime.now() + dt.timedelta(hours=hours_delta)
            exec_time()
        elif op_type == 'created_df':
            og_last = dt.datetime.now() + dt.timedelta(hours=hours_delta)
            created_df(df_list,df_rows)
        elif op_type == 'start': og_start = dt.datetime.now() + dt.timedelta(hours=hours_delta)
        elif op_type == 'rt_from_start':
            og_last = dt.datetime.now() + dt.timedelta(hours=hours_delta)
            rt = dt.datetime.now() + dt.timedelta(hours=hours_delta) - og_start
            print(ex_at_str()+' ({})'.format(rt))
        elif op_type == 'rt_from_last':
            rt = dt.datetime.now() + dt.timedelta(hours=hours_delta) - og_last
            print(ex_at_str()+' ({})'.format(rt))
            og_last = dt.datetime.now() + dt.timedelta(hours=hours_delta)
        else: print('A correct optput type has not been specified')
        #In case sound is needed, uncomment the next two lines:
        #if sound == None: next
        #else: display(Audio(filename=sound_dir+'\\'+sound, autoplay=True))
        if division != None: print(division)
    except:
        print('Excecution was completed but something went wrong when trying to show the output guide')

if __name__ == "__main__":

    og()
