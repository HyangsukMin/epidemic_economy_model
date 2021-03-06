class Config():
    def __init__(
        self,

        datetime = "20210421",
        name = "COVID_EENet_RUN_TEST5",

        ## model parameters##
        w = 14,                             # prediction period 
        h = 4,                              # multi-head
        e = 20,                             # embedding dimension
        
        seq2seq_lstm_cell = 16,
        epidemicViewFCN = 1,
        geographyViewFCN = 1,
        # macroscopicAggFCN
        activation = 'tanh',

        ## train parameters##
        epochs = 20,
        batch_size = 50,                     # should be multiple of 25.
        lr = 0.001,
        weight_decay = 0.96,
        gpu_num = 0,

        ## Input file ##
        data_dir = "../data/",
        fname_BusinessStructure_amt = "BusinessStructure_AMT.pkl",                  # Real Data is Not available
        fname_BusinessStructure_cnt = "BusinessStructure_CNT.pkl",                  # Real Data is Not available
        fname_BusinessStructure_shop_cnt = "BusinessStructure_numOfShopCNT.pkl",    # Real Data is Not available
        fname_BusinessStructure_shop_norm = "BusinessStructure_numOfShopNORM.pkl",  # Real Data is Not available
        fname_CustomerStructure = "*CustomerStructure_{}.pkl",                      # Real Data is Not available
        fname_contextual_distance = "contextual_distance_matrix.pkl",               # Real Data is Not available
        fname_physical_distance = "physical_distance.pkl",                          # Real Data is Not available
        
        fname_covid_metainfo = "seoul_mass_infection_metainfo.pkl",
        fname_covid_daily = "daily_seoul_mass_infection.pkl",
        fname_covid_cum = "cumulative_seoul_mass_infection.pkl",
        fname_covid_re_cum = "recent_cumulative_seoul_mass_infection.pkl",
        fname_elapsed_day = "covid_elapsed_day.pkl",
        
        fname_Sales2020 = "*Sales2020_AMT.pkl",                                     # Real Data is Not available
        fname_Sales2019 = "{}_Sales2019_AMT.pkl",                                   # Real Data is Not available

        ## Utility ##
        start_month = 2,                     # train start month
        end_month = 11,                      # test month
        buz_dict = {'??????_offline': 0, '????????????_offline': 1, '????????????_offline': 2, '??????/??????_offline': 3, '????????????_offline': 4, '??????_offline': 5,
                    '??????_offline': 6, '????????????_offline': 7, '????????????_offline': 8, '??????/??????_offline': 9, '??????/??????_offline': 10, '??????_offline': 11,
                    '??????/????????????_offline': 12, '??????/??????_offline': 13, '???????????????_offline': 14, '?????????_offline': 15, '????????????_offline': 16, '?????????_offline': 17,
                    '????????????_offline': 18, '???????????????_offline': 19, '??????????????????_offline': 20, '???????????????_offline': 21, '???????????????_online': 22, '????????????_offline': 23,
                    '????????????_offline': 24, '??????_offline': 25, '????????????_offline': 26, '???????????????/??????_offline': 27, '???????????????_offline': 28, '????????????_offline': 29, '??????_offline': 30,
                    '??????_offline': 31, '?????????????????????_offline': 32, '??????_offline': 33},
        city_dict = {'?????????': 0, '?????????': 1, '?????????': 2, '?????????': 3, '?????????': 4, '?????????': 5, '?????????': 6, '?????????': 7, '?????????': 8, '?????????': 9, '????????????': 10, '?????????': 11, '?????????': 12,
                     '????????????': 13, '?????????': 14, '?????????': 15, '?????????': 16, '?????????': 17, '?????????': 18, '????????????': 19, '?????????': 20, '?????????': 21, '?????????': 22, '??????': 23, '?????????': 24},
        
        n = 34,                             # the number of industries, FIXED
        m = 30,                             # the number of mass infections, 
        r = 25,                             # number of regions in Seoul, FIXED
        
        ## Save File List ##
        datapath = "../data/dataset_{}_{}.pkl",
        log_filepath = '../log',
        log_name = "training_{}_{}_{}.log",
        checkpoint_filepath = '../tmp/checkpoint/{}',
        checkpoint_model = 'training_checkpoint_{}_{}_{}',
        checkpoint_outputs = "training_checkpoint_outputs_{}_{}_{}",
        
        ## ablation ##
        ablation_economicView = True,
        ablation_geographyView = True,
        ablation_macroscopicAgg = True
    ):

        ## datetime ##
        self.datetime = datetime
        self.name = name

        ## model parameters##
        self.w = w
        self.h = h 
        self.e = e

        self.seq2seq_lstm_cell = seq2seq_lstm_cell
        self.epidemicViewFCN = epidemicViewFCN
        self.geographyViewFCN = geographyViewFCN
        self.macroscopicAggFCN = w # SHOULD BE SAME WITH w
        self.activation = activation

        ## train parameters##
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr = lr
        self.weight_decay = weight_decay
        self.gpu_num = gpu_num

        ## Input file ##
        self.data_dir = data_dir
        self.fname_BusinessStructure_amt = fname_BusinessStructure_amt
        self.fname_BusinessStructure_cnt = fname_BusinessStructure_cnt
        self.fname_BusinessStructure_shop_cnt = fname_BusinessStructure_shop_cnt
        self.fname_BusinessStructure_shop_norm = fname_BusinessStructure_shop_norm
        self.fname_CustomerStructure = fname_CustomerStructure
        self.fname_contextual_distance = fname_contextual_distance
        self.fname_physical_distance = fname_physical_distance
        self.fname_covid_metainfo = fname_covid_metainfo
        self.fname_covid_daily = fname_covid_daily
        self.fname_covid_cum = fname_covid_cum
        self.fname_covid_re_cum = fname_covid_re_cum
        self.fname_elapsed_day = fname_elapsed_day
        self.fname_Sales2020 = fname_Sales2020
        self.fname_Sales2019 = fname_Sales2019

        ## Utility ##
        self.start_month = start_month
        self.end_month = end_month
        self.buz_dict = buz_dict
        self.city_dict = city_dict
        self.m = m
        self.n = n
        self.r = r

        ## Save File List ##
        self.datapath = datapath.format(self.w, "2020-12-29")
        self.log_filepath = log_filepath
        self.log_name = log_name.format(self.datetime, self.w, self.name)
        self.checkpoint_filepath = checkpoint_filepath.format(self.name)
        self.checkpoint_model = checkpoint_model.format(self.datetime, self.w, self.name)
        self.checkpoint_outputs = checkpoint_outputs.format(self.datetime, self.w, self.name)
        
        ## ablation ##
        self.ablation_economicView = ablation_economicView
        self.ablation_geographyView = ablation_geographyView
        self.ablation_macroscopicAgg = ablation_macroscopicAgg