import React from 'react';

const DoctorsList = (props) => {
  return (
    <div>
      {
        props.doctors.map((doctor) => {
          return (
            <h4
              key={doctor.id}
              className="box title is-4"
            >{ doctor.name }
            { doctor.mail }

            </h4>
        
          )
        })
      }
    </div>
  )
};

export default DoctorsList;