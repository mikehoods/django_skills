import Link from 'next/link'

const Nav = () => {
    return (
        <nav>
            <Link href={'/'}><a>My Skills</a></Link>
            <Link href={'/add_skill'}><a>Add Skill</a></Link>
        </nav>
    )
}

export default Nav