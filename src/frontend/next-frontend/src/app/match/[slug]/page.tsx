'use client';
 
import { useRouter, usePathname, useSearchParams } from 'next/navigation';

type Params = {
    params: {
      slug: string;
    };
  };
  
 
export default function ExampleClientComponent({ params }: Params) {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();

  const { slug } = params;

  return (
    <div>
        Match {slug}
    </div>
  );

}