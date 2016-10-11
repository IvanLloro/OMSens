# Based on "standard_run_params_defaults.csv". Written as python code for
#  easier use and because this list is unlikely to change

# Pairs meaning:
#    Parameter name, value
w3_params_info_list = [("agr_inp_init",5000000000.0),
                        ("agr_mtl_toxic_index",1.0),
                        ("arable_land_init",900000000.0),
                        ("assim_half_life_1970",1.5),
                        ("avg_life_land_norm",1000.0),
                        ("des_compl_fam_size_norm",3.8),
                        ("des_food_ratio_dfr",2.0),
                        ("des_ppoll_index_DPOLX",1.2),
                        ("des_res_use_rt_DNRUR",4800000000.0),
                        ("food_short_perc_del",2.0),
                        ("fr_agr_inp_pers_mtl",0.001),
                        ("frac_res_pers_mtl",0.02),
                        ("hlth_serv_impact_del",20.0),
                        ("income_expect_avg_time",3.0),
                        ("ind_mtl_emiss_fact",0.1),
                        ("ind_mtl_toxic_index",10.0),
                        ("ind_out_in_1970",790000000000.0),
                        ("ind_out_pc_des",400.0),
                        ("industrial_capital_init",210000000000.0),
                        ("inherent_land_fert",600.0),
                        ("labor_force_partic",0.75),
                        ("labor_util_fr_del_init",1.0),
                        ("labor_util_fr_del_time",2.0),
                        ("land_fertility_init",600.0),
                        ("land_fr_harvested",0.7),
                        ("life_expect_norm",28.0),
                        ("lifet_perc_del",20.0),
                        ("max_tot_fert_norm",12.0),
                        ("nr_resources_init",1000000000000.0),
                        ("p_avg_life_agr_inp_1",2.0),
                        ("p_avg_life_agr_inp_2",2.0),
                        ("p_avg_life_ind_cap_1",14.0),
                        ("p_avg_life_ind_cap_2",14.0),
                        ("p_avg_life_serv_cap_1",20.0),
                        ("p_avg_life_serv_cap_2",20.0),
                        ("p_fioa_cons_const_1",0.43),
                        ("p_fioa_cons_const_2",0.43),
                        ("p_fr_cap_al_obt_res_2[1]",1.0),
                        ("p_fr_cap_al_obt_res_2[2]",0.2),
                        ("p_fr_cap_al_obt_res_2[3]",0.1),
                        ("p_fr_cap_al_obt_res_2[4]",0.05),
                        ("p_fr_cap_al_obt_res_2[5]",0.05),
                        ("p_fr_cap_al_obt_res_2[6]",0.05),
                        ("p_fr_cap_al_obt_res_2[7]",0.05),
                        ("p_fr_cap_al_obt_res_2[8]",0.05),
                        ("p_fr_cap_al_obt_res_2[9]",0.05),
                        ("p_fr_cap_al_obt_res_2[10]",0.05),
                        ("p_fr_cap_al_obt_res_2[11]",0.05),
                        ("p_ind_cap_out_ratio_1",3.0),
                        ("p_land_yield_fact_1",1.0),
                        ("p_nr_res_use_fact_1",1.0),
                        ("p_ppoll_gen_fact_1",1.0),
                        ("p_ppoll_tech_chg_mlt[1]",0.0),
                        ("p_ppoll_tech_chg_mlt[2]",0.0),
                        ("p_ppoll_tech_chg_mlt[3]",0.0),
                        ("p_ppoll_tech_chg_mlt[4]",0.0),
                        ("p_res_tech_chg_mlt[1]",0.0),
                        ("p_res_tech_chg_mlt[2]",0.0),
                        ("p_res_tech_chg_mlt[3]",0.0),
                        ("p_res_tech_chg_mlt[4]",0.0),
                        ("p_serv_cap_out_ratio_1",1.0),
                        ("p_serv_cap_out_ratio_2",1.0),
                        ("p_yield_tech_chg_mlt[1]",0.0),
                        ("p_yield_tech_chg_mlt[2]",0.0),
                        ("p_yield_tech_chg_mlt[3]",0.0),
                        ("p_yield_tech_chg_mlt[4]",0.0),
                        ("perc_food_ratio_init",1.0),
                        ("pers_pollution_init",25000000.0),
                        ("pop1_init",650000000.0),
                        ("pop2_init",700000000.0),
                        ("pop3_init",190000000.0),
                        ("pop4_init",60000000.0),
                        ("pot_arable_land_init",2300000000.0),
                        ("pot_arable_land_tot",3200000000.0),
                        ("ppoll_in_1970",136000000.0),
                        ("ppoll_tech_init",1.0),
                        ("ppoll_trans_del",20.0),
                        ("processing_loss",0.1),
                        ("reproductive_lifetime",30.0),
                        ("res_tech_init",1.0),
                        ("service_capital_init",144000000000.0),
                        ("social_adj_del",20.0),
                        ("social_discount",0.07000000000000001),
                        ("subsist_food_pc",230.0),
                        ("t_air_poll_time",4000.0),
                        ("t_fcaor_time",4000.0),
                        ("t_fert_cont_eff_time",4000.0),
                        ("t_ind_equil_time",4000.0),
                        ("t_land_life_time",4000.0),
                        ("t_policy_year",4000.0),
                        ("t_pop_equil_time",4000.0),
                        ("t_zero_pop_grow_time",4000.0),
                        ("tech_dev_del_TDD",20.0),
                        ("urb_ind_land_dev_time",10.0),
                        ("urban_ind_land_init",8200000.0),
                        ("yield_tech_init",1.0)]

om_TheoParamSensitivity_differentiableVariables = ['Arable_Land_Dynamics1.Arable_Land.Integrator1.y', 'Arable_Land_Dynamics1.Pot_Arable_Land.Integrator1.y', 'Arable_Land_Dynamics1.Urban_Ind_Land.Integrator1.y', 'Food_Production1.Agr_Inp.Integrator1.y', 'Food_Production1.P_Land_Yield_Fact_2.Smooth1.Integrator1.y', 'Food_Production1.P_Land_Yield_Fact_2.Smooth2.Integrator1.y', 'Food_Production1.P_Land_Yield_Fact_2.Smooth3.Integrator1.y', 'Food_Production1.Perc_Food_Ratio.Integrator1.y', 'Human_Fertility1.Avg_Ind_Out_PC.Smooth_of_Input.Integrator1.y', 'Human_Fertility1.Del_Ind_Out_PC.Smooth1.Integrator1.y', 'Human_Fertility1.Del_Ind_Out_PC.Smooth2.Integrator1.y', 'Human_Fertility1.Del_Ind_Out_PC.Smooth3.Integrator1.y', 'Human_Fertility1.Fert_Cont_Facil_PC.Smooth1.Integrator1.y', 'Human_Fertility1.Fert_Cont_Facil_PC.Smooth2.Integrator1.y', 'Human_Fertility1.Fert_Cont_Facil_PC.Smooth3.Integrator1.y', 'Human_Fertility1.Perc_Life_Expectancy.Smooth1.Integrator1.y', 'Human_Fertility1.Perc_Life_Expectancy.Smooth2.Integrator1.y', 'Human_Fertility1.Perc_Life_Expectancy.Smooth3.Integrator1.y', 'Industrial_Investment1.Industrial_Capital.Integrator1.y', 'Labor_Utilization1.Labor_Util_Fr_Del.Integrator1.y', 'Land_Fertility1.Land_Fertility.Integrator1.y', 'Land_Fertility1.Yield_Tech_LYTD.Integrator1.y', 'Life_Expectancy1.Eff_Hlth_Serv_PC.Smooth_of_Input.Integrator1.y', 'NR_Resource_Utilization1.NR_Resources.Integrator1.y', 'NR_Resource_Utilization1.P_Nr_Res_Use_Fact_2.Smooth1.Integrator1.y', 'NR_Resource_Utilization1.P_Nr_Res_Use_Fact_2.Smooth2.Integrator1.y', 'NR_Resource_Utilization1.P_Nr_Res_Use_Fact_2.Smooth3.Integrator1.y', 'NR_Resource_Utilization1.Res_Tech_NRTD.Integrator1.y', 'Pollution_Dynamics1.PPoll_Appear_Rate.Smooth1.Integrator1.y', 'Pollution_Dynamics1.PPoll_Appear_Rate.Smooth2.Integrator1.y', 'Pollution_Dynamics1.PPoll_Appear_Rate.Smooth3.Integrator1.y', 'Pollution_Dynamics1.PPoll_Tech_PTD.Integrator1.y', 'Pollution_Dynamics1.P_PPoll_Gen_Fact_2.Smooth1.Integrator1.y', 'Pollution_Dynamics1.P_PPoll_Gen_Fact_2.Smooth2.Integrator1.y', 'Pollution_Dynamics1.P_PPoll_Gen_Fact_2.Smooth3.Integrator1.y', 'Pollution_Dynamics1.Pers_Pollution.Integrator1.y', 'Population_Dynamics1.Pop_0_14.Integrator1.y', 'Population_Dynamics1.Pop_15_44.Integrator1.y', 'Population_Dynamics1.Pop_45_64.Integrator1.y', 'Population_Dynamics1.Pop_65plus.Integrator1.y', 'Service_Sector_Investment1.Service_Capital.Integrator1.y']
om_TheoParamSensitivity_params = ['agr_inp_init', 'agr_mtl_toxic_index', 'arable_land_init', 'assim_half_life_1970', 'avg_life_land_norm', 'des_compl_fam_size_norm', 'des_food_ratio_dfr', 'des_ppoll_index_DPOLX', 'des_res_use_rt_DNRUR', 'food_short_perc_del', 'fr_agr_inp_pers_mtl', 'frac_res_pers_mtl', 'hlth_serv_impact_del', 'income_expect_avg_time', 'ind_mtl_emiss_fact', 'ind_mtl_toxic_index', 'ind_out_in_1970', 'ind_out_pc_des', 'industrial_capital_init', 'inherent_land_fert', 'labor_force_partic', 'labor_util_fr_del_init', 'labor_util_fr_del_time', 'land_fertility_init', 'land_fr_harvested', 'life_expect_norm', 'lifet_perc_del', 'max_tot_fert_norm', 'nr_resources_init', 'p_avg_life_agr_inp_1', 'p_avg_life_agr_inp_2', 'p_avg_life_ind_cap_1', 'p_avg_life_ind_cap_2', 'p_avg_life_serv_cap_1', 'p_avg_life_serv_cap_2', 'p_fioa_cons_const_1', 'p_fioa_cons_const_2', 'p_fr_cap_al_obt_res_2[10]', 'p_fr_cap_al_obt_res_2[11]', 'p_fr_cap_al_obt_res_2[1]', 'p_fr_cap_al_obt_res_2[2]', 'p_fr_cap_al_obt_res_2[3]', 'p_fr_cap_al_obt_res_2[4]', 'p_fr_cap_al_obt_res_2[5]', 'p_fr_cap_al_obt_res_2[6]', 'p_fr_cap_al_obt_res_2[7]', 'p_fr_cap_al_obt_res_2[8]', 'p_fr_cap_al_obt_res_2[9]', 'p_ind_cap_out_ratio_1', 'p_land_yield_fact_1', 'p_nr_res_use_fact_1', 'p_ppoll_gen_fact_1', 'p_ppoll_tech_chg_mlt[1]', 'p_ppoll_tech_chg_mlt[2]', 'p_ppoll_tech_chg_mlt[3]', 'p_ppoll_tech_chg_mlt[4]', 'p_res_tech_chg_mlt[1]', 'p_res_tech_chg_mlt[2]', 'p_res_tech_chg_mlt[3]', 'p_res_tech_chg_mlt[4]', 'p_serv_cap_out_ratio_1', 'p_serv_cap_out_ratio_2', 'p_yield_tech_chg_mlt[1]', 'p_yield_tech_chg_mlt[2]', 'p_yield_tech_chg_mlt[3]', 'p_yield_tech_chg_mlt[4]', 'perc_food_ratio_init', 'pers_pollution_init', 'pop1_init', 'pop2_init', 'pop3_init', 'pop4_init', 'pot_arable_land_init', 'pot_arable_land_tot', 'ppoll_in_1970', 'ppoll_tech_init', 'ppoll_trans_del', 'processing_loss', 'reproductive_lifetime', 'res_tech_init', 'service_capital_init', 'social_adj_del', 'social_discount', 'subsist_food_pc', 't_air_poll_time', 't_fcaor_time', 't_fert_cont_eff_time', 't_ind_equil_time', 't_land_life_time', 't_policy_year', 't_pop_equil_time', 't_zero_pop_grow_time', 'tech_dev_del_TDD', 'urb_ind_land_dev_time', 'urban_ind_land_init', 'yield_tech_init']
