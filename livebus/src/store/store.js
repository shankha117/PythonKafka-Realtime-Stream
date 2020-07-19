import Vue from "vue";
import Vuex from "vuex";
import { latLng } from "leaflet";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    map: {
      marker1: latLng(12.98649315542851, 77.60501861572266),
      marker2: latLng(12.97194016928975, 77.53257751464844),
      marker3: latLng(12.955713422193524, 77.55695343017578)
    }
  },
  mutations: {
    update_marker_data(state, data) {
      let lat_long = latLng(data.lat, data.long);
      let m_id = data.marker_id;
      if (m_id == "1") {
        state.map.marker1 = lat_long;
      } else if (m_id == "2") {
        state.map.marker2 = lat_long;
      } else {
        state.map.marker3 = lat_long;
      }
    }
  },
  actions: {
    updatemarker(context, data) {
      console.log("this is inside actions");
      console.log(data);

      if (data.busline == "SS071") {
        this.commit("update_marker_data", {
          marker_id: "1",
          lat: data.lat,
          long: data.long
        });
      } else if (data.busline == "SS072") {
        this.commit("update_marker_data", {
          marker_id: "3",
          lat: data.lat,
          long: data.long
        });
      } else {
        this.commit("update_marker_data", {
          marker_id: "2",
          lat: data.lat,
          long: data.long
        });
      }
    }
  },
  modules: {}
});
