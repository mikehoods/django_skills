import Nav from './Nav'
import Head from 'next/head'

const Layout = (props) => (
    <div>
        <Head>
            <title>Skills App</title>
        </Head>
        <Nav/>
        {props.children}
    </div>
)

export default Layout;