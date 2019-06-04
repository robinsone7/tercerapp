import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
import UsersList from '../UsersList';

const users = [
  {
    'active': true,
    'email': 'abelthf@gmail.com',
    'id': 1,
    'username': 'fredy'
  },
  {
    'active': true,
    'email': 'abel.huanca@upeu.edu.pe',
    'id': 2,
    'username': 'abel'
  }
];

test('UsersList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
  });
