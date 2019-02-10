import * as React from 'react';
import styles from './Loader.module.css';

export interface LoaderProps {}

const Loader: React.SFC<LoaderProps> = () => {
  return (
    <div className={styles.container}>
      <div className={styles.boxOne} />
      <div className={styles.boxTwo} />
      <div className={styles.boxThree} />
    </div>
  );
};

export default Loader;
