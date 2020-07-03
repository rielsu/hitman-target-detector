import React from "react";
import GoogleMapReact from "google-map-react";

const PointPlace = ({ text }) => (
  <div
    style={{
      color: "white",
      background: "black",
      padding: "15px 5px",
      display: "inline-flex",
      textAlign: "center",
      alignItems: "center",
      justifyContent: "center",
      borderRadius: "100%",
      transform: "translate(-50%, -50%)",
    }}
  >
    {text}
  </div>
);

class SimpleMap extends React.Component {
  render() {
    return (
      <GoogleMapReact
        bootstrapURLKeys={{ key: process.env.REACT_APP_GOOGLE_MAPS_API_KEY }}
        defaultCenter={this.props.center}
        defaultZoom={1}
      >
        <PointPlace
          lat={this.props.hitmanCenter.lat}
          lng={this.props.hitmanCenter.lng}
          text={"Hitman"}
        />
        <PointPlace
          lat={this.props.targetCenter.lat}
          lng={this.props.targetCenter.lng}
          text={"Target"}
        />
      </GoogleMapReact>
    );
  }
}

export default SimpleMap;
