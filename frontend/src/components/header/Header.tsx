import * as React from 'react';
import ContentContainer from '../content-container/ContentContainer';

import styles from './Header.module.css';

export interface HeaderProps {}

const Header: React.SFC<HeaderProps> = () => {
  return (
    <ContentContainer>
      <div className={styles.team}>--force</div>
      <h1 className={styles.title}>Face Emotion</h1>
    </ContentContainer>
  );
};

export default Header;
