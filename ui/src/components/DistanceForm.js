import React from "react";

class DistanceForm extends React.Component {

  render() {
    return (
      <div>
        <form onSubmit={this.props.onSubmit}>
          
        {this.props.target.lat && (
          <button onClick={this.handleClick} className="btn btn-primary mr-4">
            Calculate Distance
          </button>
        )}
          {this.props.error && (
            <p className="text-danger">{this.props.error.message}</p>
          )}
        </form>
        {this.props.distance && (
          <p>You are at {this.props.distance} Km from target, take the jet!!</p>
        )}
      </div>
    );
  }
}

export default DistanceForm;
