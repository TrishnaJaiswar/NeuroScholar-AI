import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import TechStack from "../components/TechStack";
import About from "../components/About";
import HowItWorks from "../components/HowItWorks";
import Features from "../components/Features";
import Footer from "../components/Footer";
import Testimonials from "../components/Testimonials";
import CTA from "../components/CTA";

export default function Home() {
  return (
    <>
      <Navbar />
      <Hero />
      <TechStack />
      <About />
      <HowItWorks />
      <Features />
      <Testimonials />
      <CTA />
      <Footer />
    </>
  );
}