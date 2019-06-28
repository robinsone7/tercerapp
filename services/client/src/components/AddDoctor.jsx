import React from 'react';

const AddDoctor = (props) => {
    return(
        <form>
            <div className="field">
              <input
              name="name"
              className="input is-large"
              type="text"
              placeholder="Ingrese su nombre, doctor!"
              />
            </div>
            <div className="field">
              <input
              name="email"
              className="input is-large"
              type="email"
              placeholder="Ingrese una cuenta de correo"
              />
            </div>
           
              <input
              type="submit"
              className="button is-link is-fullwidth"
              value="Enviar"
              
              />
           

        </form>
    )
};

export default AddDoctor;