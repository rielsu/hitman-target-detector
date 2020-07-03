import React, { Component } from "react";
import SimpleMap from "../components/Map";
import TargetAddressForm from "../components/TargetAddressForm";
import DistanceForm from "../components/DistanceForm";

import "./styles/Home.css";

export default class Home extends Component {
  state = {
    loading: false,
    error: null,
    position: {
      lat: null,
      lng: null,
    },
    targetForm: {
      route: "Evergreen",
      streetNumber: "123",
      neighborhood: "",
      political: "",
      area: "",
      biggerArea: "Springfield",
      country: "US",
      postalCode: "00000",
    },
    targetCenter: {
      lat: null,
      lng: null,
    },
    hitmanCenter: {
      lat: null,
      lng: null,
    },
    euclideanDistance: null,
    myDirection: null,
  };

  handleChange = (e) => {
    this.setState({
      targetForm: {
        ...this.state.targetForm,
        [e.target.name]: e.target.value,
      },
    });
  };

  handleTargetSubmit = async (e) => {
    e.preventDefault();
    this.setState({ loading: true, error: null });
    try {
      let response = await fetch("/geocodes/geolocation/", {
        method: "post",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          street_number: this.state.targetForm.streetNumber,
          route: this.state.targetForm.route,
          neighborhood: this.state.targetForm.neighborhood,
          political: this.state.targetForm.political,
          administrative_area_level_1: this.state.targetForm.area,
          administrative_area_level_2: this.state.targetForm.biggerArea,
          country: this.state.targetForm.country,
          postal_code: this.state.targetForm.postalCode,
        }),
      });
      if (!response.ok) {
        this.setState({ loading: false, error: response.body });
        throw Error(response.status);
      }
      let responseData = await response.json();
      this.setState({
        targetCenter: {
          lat: responseData.latitude,
          lng: responseData.longitude,
        },
      });
    } catch (error) {
      this.setState({ loading: false, error: error });
    }
  };

  handleDistanceSubmit = async (e) => {
    e.preventDefault();
    this.setState({ loading: true, error: null });
    let url =
      `/geocodes/distance?start_point=${this.state.position.lat},` +
      `${this.state.position.lng}&end_point=${this.state.targetCenter.lat},` +
      `${this.state.targetCenter.lng}`;
    try {
      let response = await fetch(url, {
        method: "get",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      if (!response.ok) {
        this.setState({ loading: false, error: response.body });
        throw Error(response.status);
      }
      let responseData = await response.json();
      this.setState({ euclideanDistance: responseData.kilometers });
    } catch (error) {
      this.setState({ loading: false, error: error });
    }
  };

  handleAddressSearch = async (latitude, longitude) => {
    this.setState({ loading: true, error: null });
    try {
      let response = await fetch("/geocodes/address/", {
        method: "post",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          latitude: latitude,
          longitude: longitude,
        }),
      });
      if (!response.ok) {
        this.setState({ loading: false, error: response.body });
        throw Error(response.status);
      }
      let responseData = await response.json();
      this.setState({
        myDirection: responseData.formatted_address,
        position: {
          lat: responseData.latitude,
          lng: responseData.longitude,
        },
      });
    } catch (error) {
      this.setState({ loading: false, error: error });
    }
  };

  componentDidMount() {
    navigator.geolocation.getCurrentPosition((position) => {
      let latitude = position.coords.latitude;
      let longitude = position.coords.longitude;
      this.setState({
        hitmanCenter: {
          lat: latitude,
          lng: longitude,
        },
        position: {
          lat: latitude,
          lng: longitude,
        },
      });
      this.handleAddressSearch(latitude.toString(), longitude.toString());
    });
  }
  render() {
    return (
      <div className="Home" style={{ paddingTop: "0px" }}>
        <div className="container" style={{ marginTop: "0px" }}>
          <div className="row align-items-center" style={{ margin: "20px" }}>
            <div className=" col-6 col-md-6 col align-self-center">
              <h1>Seek and Destroy System</h1>
            </div>
            <div className=" col-6 col-md-6 col align-self-center">
              <DistanceForm
                distance={this.state.euclideanDistance}
                target={this.state.targetCenter}
                onSubmit={this.handleDistanceSubmit}
              />
            </div>
          </div>
          <div className="row">
            <div
              className=" col-7 col-md-7"
              style={{ width: "100%", height: "450px" }}
            >
              <SimpleMap
                center={this.state.position}
                targetCenter={this.state.targetCenter}
                hitmanCenter={this.state.hitmanCenter}
              />
            </div>
            <div className="Home__col col-5 col-md-5">
              <TargetAddressForm
                form={this.state.targetForm}
                onChange={this.handleChange}
                onSubmit={this.handleTargetSubmit}
              />
            </div>
            <div className="Home__col d-none d-md-block col-md-8"></div>
          </div>
        </div>
      </div>
    );
  }
}
