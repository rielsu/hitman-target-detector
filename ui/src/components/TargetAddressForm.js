import React from "react";
import "./styles/TargetAddressForm.css";

class TargetAddressForm extends React.Component {

  render() {
    return (
      <div>
        <h3>Find Your Target</h3>
        <form onSubmit={this.props.onSubmit}>
          <row>
            <div className="form-group col-3 col-md-3 TargetAddressForm__div">
              <label># St.</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="streetNumber"
                value={this.props.form.streetNumber}
              />
            </div>
            <div className="form-group col-9 col-md-9 TargetAddressForm__div">
              <label style={{ float: "right" }}>Route</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="route"
                value={this.props.form.route}
              />
            </div>
          </row>
          <row>
            <div className="form-group col-7 col-md-7 TargetAddressForm__div">
              <label>Neighborhood</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="neighborhood"
                value={this.props.form.neighborhood}
              />
            </div>
            <div className="form-group col-5 col-md-5 TargetAddressForm__div">
              <label>Political</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="political"
                value={this.props.form.political}
              />
            </div>
          </row>
          <row>
            <div className="form-group col-5 col-md-5 TargetAddressForm__div">
              <label>Area</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="area"
                value={this.props.form.area}
              />
            </div>
            <div className="form-group col-7 col-md-7 TargetAddressForm__div">
              <label style={{ float: "right" }}>Bigger Area</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="biggerArea"
                value={this.props.form.biggerArea}
              />
            </div>
          </row>
          <row>
            <div className="form-group col-8 col-md-8 TargetAddressForm__div">
              <label>Country</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="country"
                value={this.props.form.country}
              />
            </div>
            <div className="form-group col-4 col-md-4 TargetAddressForm__div">
              <label>Postal Code</label>
              <input
                onChange={this.props.onChange}
                className="form-control"
                type="text"
                name="postalCode"
                value={this.props.form.postalCode}
              />
            </div>
          </row>

          <div className="form-group col-4 col-md-4 TargetAddressForm__div">
            <button onClick={this.handleClick} className="btn btn-primary mr-4">
              Search
            </button>
          </div>

          {this.props.error && (
            <p className="text-danger">{this.props.error.message}</p>
          )}
        </form>
      </div>
    );
  }
}

export default TargetAddressForm;
