import * as React from 'react';
import styles from './ContentContainer.module.css';

export interface ContentContainerProps {
    children: React.ReactNode
}
 
const ContentContainer: React.SFC<ContentContainerProps> = ({ children }) => {
    return ( <div className={styles.root}>{children}</div> );
}
 
export default ContentContainer;